def find_majority_element(lst):
    '''Finds the element in the list that appears more than half the times.

    >>> find_majority_element([1, 2, 3, 1, 1, 1])
    1
    >>> find_majority_element([2, 1, 1])
    1
    >>> find_majority_element([1, 1, 2, 3, 4])
    Traceback (most recent call last):
    ValueError: No majority element in list.
    '''
    majority_element = None
    current_amount = 0
    # If a majority element exists, it will be found here
    for element in lst:
        if element == majority_element:
            current_amount += 1
        else:
            current_amount -= 1
            if current_amount < 0:
                majority_element = element
                current_amount = 0
    # Second loop to check that the element found is indeed a majority element.
    count = 0
    minimum_amount = len(lst) // 2
    for element in lst:
        if element == majority_element:
            count += 1
            if minimum_amount == count:
                return majority_element
    # Majority element not found
    raise ValueError('No majority element in list.')
