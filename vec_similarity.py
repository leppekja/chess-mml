from numpy import dot
from numpy.linalg import norm

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
