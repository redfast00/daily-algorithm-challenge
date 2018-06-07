from utils.prime import factorize


def count_multiplications(boardsize, number):
    '''Counts the number of occurences of number in a multiplicationtable of size boardsize.

    >>> count_multiplications(6, 12)
    4
    >>> count_multiplications(1000, 12)
    6
    >>> count_multiplications(20, 1)
    1
    >>> count_multiplications(2, 2)
    2
    >>> count_multiplications(10, 49)
    1
    >>> count_multiplications(5, 49)
    0
    '''
    assert number > 0
    if number == 1:
        return 1
    factors = factorize(number)
    first = 1
    second = number
    amount = 0
    for factor in factors:
        if first <= boardsize and second <= boardsize:
            if first == second:
                amount += 1
            else:
                amount += 2
        first *= factor
        second //= factor
    return amount
