def rotate_linked_list(node, k):
    '''Rotates a linked list k spaces to the right.

    >>> from utils.linked_list import Node
    >>> a = Node.from_list([1, 2, 3, 4, 5])
    >>> rotate_linked_list(a, 3).to_list()
    [3, 4, 5, 1, 2]
    >>> a = Node.from_list([1, 2, 3, 4, 5])
    >>> rotate_linked_list(a, 1).to_list()
    [5, 1, 2, 3, 4]
    >>> a = Node.from_list([1, 2, 3])
    >>> rotate_linked_list(a, 3).to_list()
    [1, 2, 3]
    >>> a = Node.from_list([1, 2, 3])
    >>> rotate_linked_list(a, 4).to_list()
    [3, 1, 2]
    >>> a = Node.from_list([1, 2, 3])
    >>> rotate_linked_list(a, 500 * 3 + 1).to_list()
    [3, 1, 2]
    '''

    start = node
    last = node
    length = 1
    while last.next is not None:
        last = last.next
        length += 1
    if k % length == 0:
        return start
    current = start
    for _ in range((length - (k % length) - 1)):
        current = current.next
    newstart = current.next
    current.next = None
    last.next = start
    return newstart
