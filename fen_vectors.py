import numpy as np
import pandas as pd

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

def get_position_params(fen, full_fen=True):
    """
    Encodes the last section of the FEN: active color (ac),
    castling availability (ca), en passant (ep), halfmove (hm), fullmove (fm).
    If full_fen=True, the piece placement is included, otherwise,
    assumes string "w KQkq - 0 1" only.
    Returns vector
    """
    vector = []
    if full_fen:
        pn, ac, ca, ep, hm, fm = fen.split(" ")
    else:
        ac, ca, ep, hm, fm = fen.split(" ")

    if ac == "w":
        vector.append(1)
    else:
        vector.append(0)

    castle = ['K','Q','k','q']
    if ca == "-":
        vector.extend([0] * 4)
    else:
        for j in castle:
            if j in ca:
                vector.append(1)
            else:
                vector.append(0)

    if ep == "-":
        vector.append(0)
    else:
        vector.append(1)

    vector.append(int(hm))

    vector.append(int(fm))

    return vector

def fen_to_vector(fen, board=False):
    vector = []
    piece_notations = {'p': 1,
                        'r':5,
                        'b':4,
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
    return None

def vector_to_fen(vector, board=False):
    """
    Translates a vector form board position to the fen notation.
    Does not include who's move or castling / en passant rights
    """
    fen = ''
    piece_notations = {1:'p',
                        5:'r',
                        4:'b',
                        3:'n',
                        10:'k',
                        9:'q'}

    for i, p in enumerate(vector):
        # get slashes for new row if all 8 squares obtained
        if (i != 0) & (i % 8 == 0):
            fen += '/'
        # if a piece, append it
        if p < 0:
            # black
            fen += piece_notations[np.abs(p)]
        elif p > 0:
            # white
            fen += piece_notations[p].upper()
        else:
            # square is empty
            # check if last square was empty, but make sure length > 0
            if (len(fen) > 0):
                if (fen[-1].isdigit()):
                    num = int(fen[-1])
                    #increment the last character of the fen that was the previous 0
                    fen = fen[:-1] + str(num + 1)
                else:
                    fen += '1'
            else:
                fen += '1'

    return fen


def file_fens_to_v(file, new_file_name="vec_positions.txt"):
    """
    Converts a file of fens to vectors
    """
    fens = []
    with open(file) as f:
        for l in f.readlines():
            fens.append(fen_to_vector(l))

    data = pd.DataFrame(np.row_stack(fens))
    data.to_csv("vec_positions.csv",index=False)

            
    return None

def test_fv_to_vf(fen):
    '''
    Asserts that the fen to vector and back to fen is correct,
    apart from the move and castling
    '''
    try:
        a = fen_to_vector(fen)
        b = vector_to_fen(a)
        # need to update for move / castling?
        assert b == fen.split(' ')[0]
    except Exception as e:
        print(e)
        print(fen)

def file_check(fenfile):
    """
    checks across a whole file of fens 
    """
    with open(fenfile) as f:
        for l in f.readlines():
            fv.test_fv_to_vf(l)