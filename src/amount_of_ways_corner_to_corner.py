from math import factorial


def ncr(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))


def amount_of_ways(m, n):
    '''Counts the number of ways to go from the top-left corner to
       the bottom-right corner in a (m x n) matrix by only going down and right.

    >>> amount_of_ways(2, 2)
    2
    >>> amount_of_ways(5, 5)
    70
    '''
    # Let p be the number of times we need to go right, p = n - 1
    # Let q be the number of times we need to go down, q = m - 1
    # This problem can then be simplified to choosing q out of p + q:
    return ncr(m + n - 2, n - 1)
