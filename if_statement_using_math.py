def ifstatement(a, b, y):
    '''Returns a if y == 1 or b if y == 0. a and b are 32-bit integers.
    >>> ifstatement(123, 456, 1)
    123
    >>> ifstatement(123, 456, 0)
    456
    '''
    assert y in (0, 1)
    return (a * y) + (b * (1 - y))
