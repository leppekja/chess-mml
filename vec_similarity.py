from numpy import dot, mean
from numpy.linalg import norm
import kmeans as km
import matplotlib.pyplot as plt


def vec_dot_product(pos1, pos2):
    """
    If boards are vectors, just take the dot product
    """
    return np.dot(pos1, pos2)


def row_dot_product(pos1, pos2):
    '''
    Estimates dot product for 8x8 matrices and sums
    '''
    score = 0
    for i, j in enumerate(a):
        score += np.dot(j, b[i, :])
    return score


def cosine_similarity(pos1, pos2):
    """
    Estimates the cosine of the angle between the
    vectorized positions. A returned value of O means
    the vectors are orthogonal. Position-wise, this means
    that no piece in position one is occupying a square
    that is also occupied in position 2.

    This does take into account the type of piece that is
    occupying the square, so changing a queen to a rook in
    one position, even if it is on the same square, will
    affect the similarity score.
    """
    return dot(pos1, pos2) / (norm(pos1) * norm(pos2))


def assess_clusters(data, n_clusters, verbose=False):
    model = km.kmeans(data, n_clusters=n_clusters)
    sim_scores = []
    for i in range(n_clusters):
        positions = km.return_positions(model, data, i, 50)
        scores = []
        for k in positions.itertuples():
            for j in positions.index:
                if k[0] != j:
                    scores.append(
                        cosine_similarity(list(k)[1:], positions.loc[j]))
        sim_scores.append(mean(scores))
        if verbose:
            print("For cluster", i, ", average similarity is", mean(scores))

    return sim_scores


def cartesian_product_basic(left, right):
    # https://stackoverflow.com/questions/53699012/performant-cartesian-product-cross-join-with-pandas
    return (
        left.assign(key=1).merge(right.assign(key=1), on='key').drop('key', 1))


def plot_intra_cluster_similarity(data, n_cluster_options):
    scores = []
    for i in n_cluster_options:
        scores.append(mean(assess_clusters(data, n_clusters=i)))
    plt.plot(n_cluster_options, scores)
    plt.title("Cosine Similarities between positions in a cluster")
    plt.xlabel("Cluster")
    plt.ylabel("Cosine Similarity")
    plt.show()

    return None
