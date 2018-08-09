EMPTY = 0
WALL = 1


def ways_to_bottom_corner(matrix):
    '''Finds the number of possible paths from corner to corner in a matrix.

    This finds the number of possible paths from topleft to bottomright corner where
    1's represent walls and 0's represent empty space.

    >>> ways_to_bottom_corner([[0, 0, 1], [0, 0, 1], [1, 0, 0]])
    2
    >>> ways_to_bottom_corner([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    6
    '''
    height = len(matrix) - 1
    width = len(matrix[0]) - 1
    return recursive_solver(matrix, 0, 0, height, width)


def recursive_solver(matrix, x, y, height, width):
    if x == height and y == width and matrix[x][y] == EMPTY:
        return 1
    total = 0
    if x != height and matrix[x + 1][y] == EMPTY:
        total += recursive_solver(matrix, x + 1, y, height, width)
    if y != width and matrix[x][y + 1] == EMPTY:
        total += recursive_solver(matrix, x, y + 1, height, width)
    return total
