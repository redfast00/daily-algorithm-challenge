def rotate_matrix_copy(matrix):
    '''Rotates a N*N matrix 90 degrees clockwise and returns result.

    >>> rotate_matrix_copy([
    ... [1, 2, 3],
    ... [4, 5, 6],
    ... [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    >>> rotate_matrix_copy([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]
    '''
    size = len(matrix)
    center = (size - 1)
    new_matrix = [[None] * size for _ in range(size)]
    for x in range(size):
        for y in range(size):
            new_x, new_y = get_new_coordinate(center, x, y)
            new_matrix[new_x][new_y] = matrix[x][y]
    return new_matrix


def rotate_matrix_inplace(matrix):
    '''Rotates a N*N matrix 90 degrees clockwise inplace.

    >>> rotate_matrix_copy([
    ... [1, 2, 3],
    ... [4, 5, 6],
    ... [7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    >>> rotate_matrix_copy([[1, 2], [3, 4]])
    [[3, 1], [4, 2]]
    '''
    size = len(matrix)
    center = (size - 1)
    # Middle element in odd sized matrix doesn't move
    for x in range((size + 1) // 2):
        for y in range(size // 2):
            value = matrix[x][y]
            for _ in range(4):
                new_x, new_y = get_new_coordinate(center, x, y)
                matrix[new_x][new_y], value = value, matrix[new_x][new_y]
                x, y = new_x, new_y
    return matrix


def get_new_coordinate(center, x, y):
    return y, center - x
