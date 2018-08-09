def reverse_bits(num, size=32):
    '''Reverses the bits in a number.

    >>> bin(reverse_bits(0b11001111, 8))
    '0b11110011'
    '''
    result = 0
    for idx in range(size):
        # Negative shift amounts are not allowed
        result |= (((num & 2**idx) >> idx) << (size - idx - 1))
    return result
