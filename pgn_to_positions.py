import chess
import chess.pgn

#read file
def get_games(file):
    """
    Parses a .pgn file and returns a 
    list of positions (str). 
    """
    fens = []
    game_count = 0
    num_moves = []
    with open(file) as games:
        while True:
            game = chess.pgn.read_game(games)
            position_count = 0
            if not game:
                break
            else:
                game_count += 1
                board = chess.Board()
                for move in game.mainline_moves():
                    position_count += 1
                    board.push(move)
                    fens.append(board.fen())
                    num_moves.append(position_count)

    print(game_count, "games counted.")
    print(len(fens), "positions obtained.")
    print("average of", sum(num_moves) / len(num_moves), "positions per game.")
    return fens    

def write_positions_to_file(list_of_positions, filename=None):
    """
    Writes list of positions to file with given filename.
    """
    if not filename:
        filename = "positions.txt"

    with open(filename, "w") as f:
        f.write('\n'.join(list_of_positions))
    return "File Created"