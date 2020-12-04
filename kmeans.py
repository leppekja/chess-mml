import numpy as np
import pandas as pd
import fen_vectors as fv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize


def pca(data_csv, n_components):
    """
    Perform PCA on the data and return the
    transformed data in a tuple (model, data)
    """
    data = pd.read_csv(data_csv)
    pca = PCA(n_components=n_components)
    pca.fit(data)
    print(pca.explained_variance_ratio_)
    print(pca.singular_values_)
    return (pca, pca.transform(data))


def kmeans(data, csv=True, n_clusters=3, n_init=10, max_iter=300, normalization=True):
    """
    Initialize KMeans classifier
    """
    if csv:
        data = pd.read_csv(data)

    if normalization:
        # using l2 norm to normalize each sample
        # may pass in already normalized data;
        # if so, use False in function args
        normalize(data, copy=False, return_norm=False)

    kmeans = KMeans(n_clusters=n_clusters,
                    n_init=n_init,
                    max_iter=max_iter).fit(data)
    return kmeans


def classify_pos(model, pca=None, fen_string=None):
    """
    Classify a single position to a group with
    a trained model.
    """
    assert fen_string is not None, "Need a FEN"

    # Need to reshape for a single sample, avoid Value Error
    v = fv.fen_to_vector(fen_string).reshape(1, -1)

    if pca:
        v = pca.transform(v)

    return model.predict(v)


def return_positions(model, data_csv, group, num_to_return):
    """
    Return a specified number of positions from a group.
    """
    data = pd.read_csv(data_csv)
    group_indices = get_indices(group, model.labels_)
    return data.iloc[group_indices].sample(num_to_return)


def positions_to_fens(positions):
    return positions.apply(fv.vector_to_fen, axis=1)


def get_indices(clustNum, labels_array):
    """
    Helper function for return_positions function.
    credit to https://stackoverflow.com/questions/36195457/python-sklearn-kmeans-how-to-get-the-samples-points-in-each-clusters
    """
    return np.where(labels_array == clustNum)[0]


def plot_curve(data_csv, n_clusters_options=3, n_init=10, max_iter=300, normalization=True):
    """
    tries multiple options of k (list)
    https://stackoverflow.com/questions/41540751/sklearn-kmeans-equivalent-of-elbow-method
    """
    data = pd.read_csv(data_csv)
    if normalization:
        # Normalize data set only once, rather than over and over again
        normalize(data, copy=False, return_norm=False)
    # list comprehension to create a model for each k
    clusters = [kmeans(data=data,
                       csv=False,
                       n_clusters=k,
                       n_init=n_init,
                       max_iter=max_iter,
                       normalization=not normalization) for k in n_clusters_options]
    # three methods
    scores = [i.score(data) for i in clusters]
    inertias = [i.inertia_ for i in clusters]
    distances = [np.average(np.min(cdist(data, i.cluster_centers_, 'euclidean'), axis=1))
                 for i in clusters]
    # plot
    fig, axs = plt.subplots(3)
    fig.suptitle('curves')
    axs[0].plot(n_clusters_options, scores)
    axs[0].set_title('sklean scores')
    axs[1].plot(n_clusters_options, inertias)
    axs[1].set_title('inertias?')
    axs[2].plot(n_clusters_options, distances)
    axs[2].set_title('distances from each cluster center')
    plt.show()
    return (n_clusters_options, scores, inertias, distances)
