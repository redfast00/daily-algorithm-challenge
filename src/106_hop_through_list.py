def can_make_jumps(lst):
    '''Determines if we can jump to the end of the list.

    Every number in the list stands for the maximum number of hops we can make
    from that index.

    >>> can_make_jumps([1])
    True
    >>> can_make_jumps([0])
    True
    >>> can_make_jumps([2, 0, 1, 0])
    True
    >>> can_make_jumps([1, 1, 0, 1])
    False
    >>> can_make_jumps([5, 0, 0, 0])
    True
    >>> can_make_jumps([0, 1, 1, 1])
    False
    >>> can_make_jumps([1, 1, 0])
    True
    '''

    steps_left = 1
    for new_jump in lst:
        if steps_left == 0:
            return False
        steps_left = max(steps_left - 1, new_jump)
    return True
