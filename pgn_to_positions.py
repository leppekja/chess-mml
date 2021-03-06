import chess
import chess.pgn

# read file


def get_games(file, num_games_to_get=None, ratings=False):
    """
    Parses a .pgn file and returns a
    list of positions (str). If num_games_to_get
    is None, returns all games.
    """
    fens = []
    ratingslist = []
    game_count = 0
    num_moves = []
    with open(file) as games:
        while True:
            game = chess.pgn.read_game(games)

            position_count = 0
            if not game:
                break
            else:
                if ratings:
                    welo = game.headers['WhiteElo']
                    belo = game.headers['BlackElo']
                    diff = int(welo) - int(belo)
                game_count += 1
                board = chess.Board()
                for move in game.mainline_moves():
                    position_count += 1
                    board.push(move)
                    fens.append(board.fen())
                    if ratings:
                        ratingslist.append(diff)
                    num_moves.append(position_count)
                if game_count == num_games_to_get:
                    break

    print(game_count, "games counted.")
    print(len(fens), "positions obtained.")
    print("average of", sum(num_moves) / len(num_moves), "positions per game.")
    if ratings:
        return (fens, ratingslist)
    else:
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
