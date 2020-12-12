import kmeans as km
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d
from sklearn.decomposition import PCA


def pca_and_plot(ndims):
    """
    Perform 2 or 3d PCA and plot. Colored by the number of pieces
    on the board.
    """

    dall = pd.read_csv("vec_positions.csv")
    # Get # of pieces on the board
    dall.ne(0).sum(axis=1)

    if ndims == 2:
        pca, data = km.pca("vec_positions.csv", 2)

        d = pd.DataFrame(data)
        d['numpieces'] = dall.ne(0).sum(axis=1)

        plt.scatter(d[0], d[1], s=2, c=d.iloc[:, 2])

    elif ndims == 3:
        ax = plt.axes(projection="3d")
        pca, data = km.pca("vec_positions.csv", 3)

        d = pd.DataFrame(data)
        d['numpieces'] = dall.ne(0).sum(axis=1)

        ax.scatter(d[0], d[1], d[2], s=2, c=d.iloc[:, 3])

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    # if ndims == 3:
    #     plt.zlabel("Feature 3")

    plt.title("PCA on Position Dataset")
    plt.show()

    return None


def visualize_clusters(data, n_clusters):
    """
    Performs PCA on 500 samples from each cluster and plots
    with color being the group label.
    """
    model = km.kmeans(data, n_clusters=n_clusters)
    dfs = []
    for c in range(n_clusters):
        dfs.append(km.return_positions(model, "vec_positions.csv", c,  500))
    df = pd.concat(dfs)
    pca = PCA(2)
    pca.fit(df)
    pcadf = pd.DataFrame(pca.transform(df))
    pcadf['group'] = 1
    for i in range(len(dfs)):
        pcadf.loc[500 * i:500 + (500 * i), 'group'] = i + 1
    sns.scatterplot(pcadf[0], pcadf[1], hue=pcadf['group'], palette="bright")
    plt.show()
    return None
