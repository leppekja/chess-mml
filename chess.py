import numpy as np

c = np.array([[ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1., 10.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1., 10.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  9.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.],
                [ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.]])

# Create a 8x8 matrix where empty squares have the value of 1,
# pawns 2, knight 4, bishop 4, rook 6, queen 9, king 10

def row_dot_product(pos1, pos2):
    score = 0
    for a in pos1:
        for b in pos2:
            score += np.dot(a, b)

    for i, j in enumerate(a):
        np.dot(j, b[i, :])