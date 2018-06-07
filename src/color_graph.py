import itertools


def color_matrix(matrix, k):
    '''Determines if a undirected graph can be colored in k colors given an adjacency matrix.

    If matrix[i][j] is True, then i and j are connected.
    >>> color_matrix([[1, 1], [1, 1]], 1)
    False
    >>> color_matrix([[1, 1], [1, 1]], 2)
    True
    '''
    return backtrack(matrix, k, [None] * len(matrix), 0)


def backtrack(matrix, k, coloring, current):
    if current == len(matrix):
        return True
    for candidate in range(k):
        for idx, is_connected in enumerate(itertools.islice(matrix[current], current)):
            if is_connected and coloring[idx] == candidate:
                break
        else:
            # Found a color, add current color to the coloring
            coloring[current] = candidate
            result = backtrack(matrix, k, coloring, current + 1)
            if result:
                return True
    return False
