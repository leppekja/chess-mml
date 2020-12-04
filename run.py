import vec_similarity as vs
import kmeans as km
import fen_vectors as fv
import argparse
import pandas as pd

parser = argparse.ArgumentParser(
    description="Read PGNs and obtain similar positions.")
parser.add_argument("-file")
parser.add_argument("-fen",
                    action='append',
                    help="One position to return similar positions to")

args = parser.parse_args()


if __name__ == "__main__":
    model = km.kmeans(args.file)
    pred = km.classify_pos(model, fen_string=args.fen[0])
    positions = pd.DataFrame(
        km.return_positions(
            model,
            args.file,
            pred,
            50
        )
    )

    scores = pd.Series(positions.apply(
        vs.cosine_similarity, args=(
            fv.fen_to_vector(args.fen[0]),), axis=1))
    positions = pd.DataFrame(km.positions_to_fens(positions))
    positions['similarity'] = scores
    positions.to_csv("similar_positions.csv", index=False)
