def swap_even_and_odd_bits(n):
    '''Swaps the even and odd bits of an unsigned, 8-bits number.

    >>> swap_even_and_odd_bits(0b10101010) == 0b01010101
    True
    >>> swap_even_and_odd_bits(0b11100010) == 0b11010001
    True
    '''
    assert 0 <= n <= 0xFF, 'Not an 8-bit unsigned number'
    return ((n & 0b10101010) >> 1) | ((n & 0b01010101) << 1)
