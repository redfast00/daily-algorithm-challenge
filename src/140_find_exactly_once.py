def find_exactly_once(lst):
    '''All numbers in lst appear exactly twice, except one. Finds that one number.

    >>> find_exactly_once([1, 1, 2])
    2
    >>> find_exactly_once([1, 2, 3, 2, 1])
    3
    '''
    current = 0
    for number in lst:
        # XOR
        current ^= number
    return current
