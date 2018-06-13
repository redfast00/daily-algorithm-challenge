def is_rotated(first, second):
    '''Checks if second is a rotation of first.

    >>> is_rotated('this is a test', 'is a testthis ')
    True
    >>> is_rotated('abcdef', 'fabcde')
    True
    >>> is_rotated('abc', 'cba')
    False
    >>> is_rotated('aaaa', 'a')
    False
    >>> is_rotated('aaaab', 'baaaa')
    True
    '''
    if len(first) != len(second):
        return False
    for rotation in range(len(first)):
        for idx in range(len(first)):
            if first[idx] != second[(idx + rotation) % len(second)]:
                break
        else:
            return True
    return False
