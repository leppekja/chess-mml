# chess-mml
Project for Math for Machine Learning

[FEN Notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)



### Fen to Vector representation:
Using: "rn1qkbnr/pppb1ppp/4p3/3p4/5P2/2N2N2/PPPPP1PP/R1BQKB1R w KQkq - 0 1" returns a (64, ) shape vector. Can enter board = True to return a 8x8 array. 

Note this function does not include which player to move, castling rights, en passant, and move counts. This is the " w KQkq - 0 1" part of the notation. Function stops interpreting when it hits the end of the board representation. 

### PGN to positions
Writes a file of PGNs to FEN notation using python-chess, and returns a text file.