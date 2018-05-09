from utils.linked_list import Node


def reverse_linked_list(node):
    '''Reverses a singly-linked list in-place.
    >>> reverse_linked_list(Node.from_list([1, 2, 3, 4])).to_list()
    [4, 3, 2, 1]
    '''
    previous = None
    while node is not None:
        next_node = node.next
        node.next = previous
        previous = node
        node = next_node
    return previous
