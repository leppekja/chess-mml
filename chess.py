import numpy as np

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


def fen_to_vector(fen, board=False):
    vector = []
    piece_notations = {'p': 1,
                        'r':5,
                        'b':3,
                        'n':3,
                        'k':10,
                        'q':9}
    for p in fen:
        if p == " ":
            break
        elif p.isdigit():
            vector.extend([0] * int(p))
        else:
            if p.isupper():
                vector.append(piece_notations[p.lower()])
            elif p.islower():
                vector.append(piece_notations[p] * -1)
    if board:
        return np.array(vector).reshape((8,8))
    else:
        return np.array(vector)
        