def amount_of_elements_smaller(matrix, i, j):
    '''Count the amount of elements smaller than m[i][j] in the (square) matrix.

    Each column and row is sorted in ascending order.
    >>> amount_of_elements_smaller([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1)
    4
    '''
    size = len(matrix)
    assert size == len(matrix[0])
    split = matrix[i][j]
    jdx = size - 1
    amount = 0
    for idx in range(size):
        while matrix[idx][jdx] >= split:
            jdx -= 1
            if jdx < 0:
                return amount
        amount += jdx + 1
    return amount
