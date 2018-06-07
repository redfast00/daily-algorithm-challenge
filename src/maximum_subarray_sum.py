def maximum_subarray_sum(lst):
    '''Finds the maximum sum of all subarrays in lst in O(n) time and O(1) additional space.

    >>> maximum_subarray_sum([34, -50, 42, 14, -5, 86])
    137
    >>> maximum_subarray_sum([-5, -1, -8, -101])
    0
    '''
    current_sum = 0
    maximum_sum = 0
    for value in lst:
        current_sum = max(current_sum + value, 0)
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum
