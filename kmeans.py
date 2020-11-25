import numpy as np
import pandas as pd
import fen_vectors as fv
from sklearn.cluster import KMeans

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