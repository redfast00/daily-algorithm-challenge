def find_duplicate(lst):
    '''Given a list of lenght n + 1 with elements in {1, 2, ..., n}, find a duplicate element.

    This has to be done in linear time and space.

    >>> find_duplicate([1, 3, 2, 1])
    1
    >>> find_duplicate([1, 3, 2, 3])
    3
    >>> find_duplicate([1, 2, 2, 3])
    2
    '''
    found = set()
    for element in lst:
        assert (element in range(len(lst))), 'not in range'
        # Checking if an element is in a set takes constant time
        if element in found:
            return element
        # Adding an element to a set takes constant time
        # This set will never be bigger than n items, so linear space
        found.add(element)
    raise ValueError('This is impossible due to the pigeonhole principle')
