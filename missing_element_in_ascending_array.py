def find_missing_element(lst):
    '''Finds the first positive integer that is not in lst
    >>> find_missing_element([2])
    1
    >>> find_missing_element([3, 2, 1])
    4
    >>> find_missing_element([3, 4, -1, 1])
    2
    >>> find_missing_element([1, 2, 0])
    3
    '''
    max_ = len(lst)
    # reorder list
    # [3, 4, -1, 1] -> [1, -1, 3, 4]
    current_idx = 0
    current_element = lst[current_idx]
    while (current_idx < max_ - 1):
        if 0 < current_element <= max_:
            # check if element is already in it's place
            if current_element == lst[current_element - 1]:
                current_idx += 1
                current_element = lst[current_idx]
                continue
            elif 0 < lst[current_element - 1] <= max_:
                c = current_element
                current_element = lst[c - 1]
                lst[c - 1] = c
            else:
                lst[current_element - 1] = current_element
                current_idx += 1
                current_element = lst[current_idx]
        else:
            current_idx += 1
            current_element = lst[current_idx]

    # find first element that is incorrect
    for i in range(0, max_):
        if lst[i] != i + 1:
            return i + 1
    return max_ + 1
