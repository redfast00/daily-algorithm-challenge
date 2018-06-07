def find_contiguous_sum(numbers, sum):
    '''Finds a contiguous subarray of numbers that has a sum of sum.

    >>> find_contiguous_sum([1, 2, 3, 4, 5], 9)
    [2, 3, 4]
    >>> find_contiguous_sum([2, -3, 4, -10], -9)
    [-3, 4, -10]
    >>> find_contiguous_sum([5, 6, 8], 3)
    >>> find_contiguous_sum([1, 2, 3], 20)
    >>> find_contiguous_sum([1, 2, 3, 102], 102)
    [102]
    >>> find_contiguous_sum([1, 2, 3], 6)
    [1, 2, 3]
    '''
    current_sum = 0
    # This works by essentially subtracting two ranges of numbers:
    #  if you subtract everything up to the begin index from everything up to and including the
    #  end index, you get the sum of everything from the begin index to the end index.
    # This can be done efficiently by storing all sums up to an index i in a map.

    # 0 can be made as sum of no elements (= sum of all elements before index 0)
    already_found = {0: -1}
    for idx, element in enumerate(numbers):
        current_sum += element
        if (current_sum - sum) in already_found:
            begin = already_found[current_sum - sum]
            return numbers[begin + 1: idx + 1]
        already_found[current_sum] = idx
