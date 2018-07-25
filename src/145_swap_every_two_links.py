def swap_every_two_links(linked_list):
    '''Swaps every two nodes in a linked list

    >>> from utils.linked_list import Node
    >>> linked = Node.from_list([1, 2, 3, 4, 5, 6])
    >>> swap_every_two_links(linked).to_list()
    [2, 1, 4, 3, 6, 5]
    >>> swap_every_two_links(Node.from_list([1, 2])).to_list()
    [2, 1]
    >>> swap_every_two_links(Node.from_list([0])).to_list()
    [0]
    >>> swap_every_two_links(Node.from_list([1, 2, 3, 4, 5])).to_list()
    [2, 1, 4, 3, 5]
    '''
    first = linked_list
    # Check that there are enough links to start reversing
    if first is None or first.next is None:
        return first
    second = first.next
    retval = second
    # Draw this on paper, it helps you understand
    while second.next is not None and second.next.next is not None:
        nextfirst = second.next
        nextsecond = second.next.next
        second.next = first
        first.next = nextsecond
        first, second = nextfirst, nextsecond
    nextfirst = second.next
    second.next = first
    first.next = nextfirst
    return retval
