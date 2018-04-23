def round_upper_power_of_two(x):
    '''Rounds up to smallest power of two.

    >>> round_upper_power_of_two(60)
    64
    >>> round_upper_power_of_two(128)
    128
    '''
    return 2**(x-1).bit_length()


def find_in_rotated_array(arr, element):
    '''Finds the index of an element in a rotated sorted array in O(log n) time.

    >>> find_in_rotated_array([0, 1, 2, 3, 4, 5], 4)
    4
    >>> find_in_rotated_array([3, 4, 5, 0, 1, 2], 2)
    5
    >>> find_in_rotated_array([1, 5, 6, 8, 0], 4)
    >>> find_in_rotated_array([1, 2], 2)
    1
    >>> find_in_rotated_array([5], 5)
    0
    '''
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return 0 if element == arr[0] else None

    current_idx = 0
    step_size = round_upper_power_of_two(len(arr))
    arr_size = len(arr)

    while step_size > 0:
        step_size = (step_size) // 2
        current = arr[current_idx]
        if element == current:
            return current_idx
        elif element > current:
            current_idx = (current_idx + step_size) % arr_size
        else:
            current_idx = (current_idx - step_size) % arr_size
