from collections import Counter


def count_attacking_bishops(bishops, size):
    '''Counts amount of attacks with bishops on a chessboard where attacks pass trough pieces.

    >>> count_attacking_bishops([(0, 0), (1, 2), (2, 2), (4, 0)], 5)
    2
    '''
    first_diagonal = Counter()
    second_diagonal = Counter()
    for (x, y) in bishops:
        first_diagonal[x - y] += 1
        second_diagonal[x + y] += 1

    total = 0
    for counter in (first_diagonal, second_diagonal):
        for key, amount in counter.items():
            total += ((amount - 1) * amount) // 2
    return total
