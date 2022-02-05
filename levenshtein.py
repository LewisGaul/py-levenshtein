__all__ = ("distance", "ratio")

import sys


def distance(word1: str, word2: str) -> float:
    # Initialise the matrix.
    distances = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for t1 in range(len(word1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(word2) + 1):
        distances[0][t2] = t2

    # Fill in the distances.
    for i1, c1 in enumerate(word1, start=1):
        for i2, c2 in enumerate(word2, start=1):
            if c1 == c2:
                d = distances[i1 - 1][i2 - 1]
            else:
                d = 1 + min(
                    distances[y][x]
                    for (y, x) in [(i1 - 1, i2 - 1), (i1 - 1, i2), (i1, i2 - 1)]
                )
            distances[i1][i2] = d

    return distances[-1][-1]


def ratio(word1: str, word2: str) -> float:
    lensum = len(word1) + len(word2)
    return 1 - distance(word1, word2) / lensum


if __name__ == "__main__":
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    print("Distance:", distance(word1, word2))
    print("Ratio: {:.3f}".format(ratio(word1, word2)))
