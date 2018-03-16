from utils.linked_list import Node


def find_intersection(first, second):
    '''Finds the element where the first and second linked list collide.
    >>> common = Node.from_list([5, 100, 203])
    >>> first = Node.from_list([1, 2, 3, 86, 7], common)
    >>> second = Node.from_list([30, 35], common)
    >>> find_intersection(first, second)
    5
    '''
    # Make linked lists the same length
    first_len = find_linked_list_length(first)
    second_len = find_linked_list_length(second)
    while first_len > second_len:
        first = first.next
        first_len -= 1
    while second_len > first_len:
        second -= second.next
        second_len -= 1

    # Loop over linked lists at the same time until element that is the same
    while first != second:
        first = first.next
        second = second.next

    # first and second are either same node or None
    if first is None:
        return None
    else:
        return first.value


def find_linked_list_length(ll):
    length = 0
    while ll is not None:
        ll = ll.next
        length += 1
    return length
