def largest_non_adjacent_sum(arr):
    '''Finds the largest sum of two non-adjacent numbers.
    >>> largest_non_adjacent_sum([1, 2, 3])
    4
    >>> largest_non_adjacent_sum([5, 1, 1, 5])
    10
    >>> largest_non_adjacent_sum([2, 4, 6, 8])
    12
    '''
    assert len(arr) >= 3, 'List needs to have at least three elements'
    # a solution in O(n^2)
    max_ = -float('inf')
    for first_idx in range(0, len(arr) - 1):
        for second_idx in range(first_idx + 2, len(arr)):
            max_ = max(max_, arr[first_idx] + arr[second_idx])
    return max_