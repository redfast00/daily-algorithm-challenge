import heapq


def largest_product(numbers):
    '''Returns the maximum product of three integers in the list.

    >>> largest_product([-10, -10, 5, 2])
    500
    >>> largest_product([5, 2, 3])
    30
    >>> largest_product([-5, -4, 3, 2, 4])
    80
    >>> largest_product([-5, -6, -1, -2])
    -10
    '''
    assert len(numbers) >= 3, 'Not enough numbers'
    large = heapq.nlargest(3, numbers)
    small = heapq.nsmallest(2, numbers)

    return max(large[0] * large[1] * large[2], small[0] * small[1] * large[0])
