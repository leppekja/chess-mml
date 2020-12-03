import kmeans as km
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def pca_and_plot(ndims):
    """
    Perform 2d PCA and plot, with colors as 
    the number of pieces on the board. 
    """
    # Get # of pieces on the board
    dall = pd.read_csv("vec_positions.csv")
    dall.ne(0).sum(axis=1)

    if ndims == 2:
        pca, data = km.pca("vec_positions.csv", 2)

        d = pd.DataFrame(data)
        d['numpieces'] = dall.ne(0).sum(axis=1)

        plt.scatter(d[0],d[1],s=2,c=d['numpieces'])
    
    elif ndims == 3:
        ax = plt.axes(projection="3d")
        pca, data = km.pca("vec_positions.csv", 3)
        
        d = pd.DataFrame(data)
        d['numpieces'] = dall.ne(0).sum(axis=1)

        ax.scatter(d[0],d[1],d['numpieces'], s=2,c=d['numpieces'])

    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    if ndims == 3:
        plt.zlabel("Number of Pieces")
    
    plt.title("PCA on Position Dataset")
    plt.show()

    return None