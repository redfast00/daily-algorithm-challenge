def stream_bits(n):
    p = 1
    while p <= n:
        bit = (n & p) != 0
        p *= 2
        yield bit


def custom_pow(x, y):
    '''Custom pow implementation using repeated squaring.

    >>> custom_pow(2, 5)
    32
    >>> custom_pow(2, 10)
    1024
    >>> custom_pow(2, 0)
    1
    >>> custom_pow(2, 2)
    4
    '''
    result = 1
    current = x
    for bit in stream_bits(y):
        if bit:
            result *= current
        current *= current
    return result
