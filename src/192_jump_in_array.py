def jump_in_array(lst):
    '''Given an array of non-negative numbers, determine if we can jump out of the end of the array.

    We can jump at most the amount of places as the number we are on.

    >>> jump_in_array([1])
    True
    >>> jump_in_array([1] * 20)
    True
    >>> jump_in_array([1, 0])
    False
    >>> jump_in_array([2, 0, 1])
    True
    '''

    jumps_left = 0
    for jump_amount in lst:
        jumps_left = max(jumps_left, jump_amount)
        jumps_left -= 1
        if jumps_left < 0:
            return False
    return True
