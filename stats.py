import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def occupied_frequencies(positions, returnfreqs=False):
    '''
    Creates heatmap for how often a square is 
    occupied given a list of positions.
    Uses vectorized positions. Returns None by default.
    '''
    xcoords = ['NA','a','b','c','d','e','f','g','h']
    ycoords = ['NA', 8, 7, 6, 5, 4, 3, 2, 1]
    v = pd.read_csv(positions)
    r, c = v.shape
    # Check if a piece is on each square (nonzero)
    # and divide by number of positions
    freqs = np.array((v.astype(bool).sum(axis=0)) / r).reshape((8,8))
    f, ax = plt.subplots()

    # chessboard overlay
    # https://matplotlib.org/3.1.1/gallery/images_contours_and_fields/layer_images.html#sphx-glr-gallery-images-contours-and-fields-layer-images-py
    #extent = np.min(x), np.max(x), np.min(y), np.max(y)
    cb = np.add.outer(range(8), range(8)) % 2
    ax.imshow(cb, cmap=plt.cm.gray, interpolation='nearest',
                 extent=(-.5,7.5,-.5,7.5), alpha=.3)

    # frequencies
    ax.imshow(freqs,interpolation="bilinear", alpha=.9)

    # text annotations
    for i in range(8):
        for j in range(8):
            text = ax.text(j, i, freqs[i, j].round(2),
                        ha="center", va="center", color="w")

    ax.set_title("Frequency of Occupied Squares")
    ax.set_xticklabels(xcoords)
    ax.set_yticklabels(ycoords)
    plt.show()

    if returnfreqs:
        return freqs

    return None

def most_common_squares_for_pieces(positions):
    """
    Creates visualizations for the most commonly occupied squares,
    by piece type. 
    The starting positions dominate the visualized boards here.
    """
    piece_notations = {1:'pawn',
                    5:'rook',
                    4:'bishop',
                    3:'knight',
                    10:'king',
                    9:'queen'}

    xcoords = ['a','b','c','d','e','f','g','h']
    ycoords = [8, 7, 6, 5, 4, 3, 2, 1]

    fig, axs = plt.subplots(2, 6, sharex=True, sharey=True)
    plt.setp(axs, xticks=range(0,9), xticklabels=xcoords,
                    yticks=range(0,9), yticklabels=ycoords)
    v = pd.read_csv(positions)
    r, c = v.shape

    # Get absolute counts and divide by count of positions
    counts = v.apply(pd.Series.value_counts) / r
    
    counts.fillna(0, inplace=True)
    # Don't want empty spaces
    counts.drop(0, inplace=True)

    #chessboard underlay
    cb = np.add.outer(range(8), range(8)) % 2


    for ax, index in zip(axs.flat, counts.index):

        ax.imshow(cb, cmap=plt.cm.gray, interpolation='nearest',
                 extent=(-.5,7.5,-.5,7.5), alpha=.3)

        ax.imshow(np.array(counts.loc[index]).reshape((8,8)), 
                            interpolation='bilinear', alpha=.9)

        ax.set_title(piece_notations[np.abs(index)])
        # ax.set_xticklabels(xcoords)
        # ax.set_yticklabels(ycoords)

    plt.tight_layout()
    fig.suptitle("Most commonly occupied squares by piece type")
    axs[0, 0].set_ylabel("Black")
    axs[1, 0].set_ylabel("White")
    plt.show()






