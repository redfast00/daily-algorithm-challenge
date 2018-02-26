def product_in_array(lst):
    '''Each element of the result is the product of all elements in lst except
       the one at the index of the original element.
    >>> product_in_array([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]
    >>> product_in_array([])
    []
    >>> product_in_array([503])
    [1]
    '''
    result = [1] * len(lst)
    # Forward
    current = 1
    for idx in range(1, len(lst)):
        current *= lst[idx - 1]
        result[idx] = current
    # Reverse
    current = 1
    for idx in range(len(lst) - 2, -1, -1):
        current *= lst[idx + 1]
        result[idx] *= current
    return result
