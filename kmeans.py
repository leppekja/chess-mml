import numpy as np
import pandas as pd
import fen_vectors as fv
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

def kmeans(data_csv, num_clusters):
    """
    Initialize KMeans classifier
    """
    data = pd.read_csv(data_csv)
    kmeans = KMeans(n_clusters=num_clusters).fit(data)
    return kmeans

def classify_pos(model, fen_string):
    """
    Classify a single position to a group with
    a trained model. 
    """
    v = fv.fen_to_vector(fen_string)
    return model.predict(v.reshape(1,-1))

def return_positions(model, data_csv, group, num_to_return):
    """
    Return a specified number of positions from a group.
    """
    data = pd.read_csv(data_csv)
    group_indices = get_indices(group, model.labels_)
    return data.iloc[group_indices].sample(num_to_return)

def positions_to_fens(positions):
    return positions.apply(fv.vector_to_fen, axis = 1)

def get_indices(clustNum, labels_array): 
    """
    Helper function for return_positions function.
    credit to https://stackoverflow.com/questions/36195457/python-sklearn-kmeans-how-to-get-the-samples-points-in-each-clusters
    """
    return np.where(labels_array == clustNum)[0]


def plot_curve(k_options, data_csv):
    """
    tries multiple options of k (list)
    https://stackoverflow.com/questions/41540751/sklearn-kmeans-equivalent-of-elbow-method
    """
    data = pd.read_csv(data_csv)
    clusters = [KMeans(n_clusters=i).fit(data) for i in k_options]
    # three methods
    scores = [i.score(data) for i in clusters]
    inertias = [i.inertia_ for i in clusters]
    distances = [np.average(np.min(cdist(data, i.cluster_centers_, 'euclidean'), axis=1)) for i in clusters]
    #plot
    fig, axs = plt.subplots(3)
    fig.suptitle('curves')
    axs[0].plot(k_options, scores)
    axs[0].set_title('sklean scores')
    axs[1].plot(k_options, inertias)
    axs[1].set_title('inertias?')
    axs[2].plot(k_options, distances)
    axs[2].set_title('distances from each cluster center')
    plt.show()
    return (k_options, scores, inertias, distances)