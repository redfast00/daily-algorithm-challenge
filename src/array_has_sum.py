def array_has_sum(lst, k):
    '''Returns whether a list lst contains two numbers that add up to k.
    >>> array_has_sum([10, 15, 3, 7], 17)
    True
    >>> array_has_sum([17, 18], 17)
    False
    >>> array_has_sum([1,1,1,5], 2)
    True
    >>> array_has_sum([12, 13], 25)
    True
    >>> array_has_sum([], 12)
    False
    >>> array_has_sum([17], 17)
    False
    '''
    # Sort list, but don't overwrite it
    lst = sorted(lst)
    begin = 0
    end = len(lst) - 1
    while begin < end:
        sum_ = lst[begin] + lst[end]
        if sum_ < k:
            begin += 1
        elif sum_ > k:
            end -= 1
        else:
            # Not smaller, not bigger, so must be equal
            return True
    return False
