from utils import INFINITY


def maximum_matrix_path_sum(matrix):
    '''Returns the maximum amount of 'coins' on the path.

    The path taken is a shortest path from the upper-left corner to the bottom-right corner.

    >>> maximum_matrix_path_sum([[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]])
    12
    '''
    height = len(matrix)
    width = len(matrix[0])
    new_matrix = [[None for _ in range(width)] for _ in range(height)]
    return get_parent(matrix, new_matrix, height - 1, width - 1, width, height)


def get_parent(matrix, new_matrix, x, y, width, height):
    # This is kinda inefficent, this can be done with two nested for-loops
    # Using for-loops doesn't have the overhead of the callstack
    max_ = -INFINITY
    # Calculate 'parents'
    for dx, dy in ((-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if nx in range(height) and ny in range(width):
            if new_matrix[nx][ny] is None:
                new_matrix[nx][ny] = get_parent(matrix, new_matrix, nx, ny, width, height)
            max_ = max(new_matrix[nx][ny], max_)
    if max_ == -INFINITY:
        return matrix[x][y]
    return max_ + matrix[x][y]
