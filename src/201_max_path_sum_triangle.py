def max_path_sum(triangle):
    '''Calculates the maximum path sum in a triangle

    You have to go from the top of the triangle to the bottom
    >>> max_path_sum([[1], [0, 2], [100, 2, 3]]) # we choose left, then left
    101
    >>> max_path_sum([[20]])
    20
    '''
    for layeridx in range(len(triangle) - 2, 0, -1):
        assert len(triangle[layeridx]) == layeridx + 1, "Expects a triangle"
        for columnidx in range(layeridx):
            below = layeridx + 1
            triangle[layeridx][columnidx] = max(triangle[below][columnidx],
                                                triangle[below][columnidx + 1])
    return triangle[0][0]
