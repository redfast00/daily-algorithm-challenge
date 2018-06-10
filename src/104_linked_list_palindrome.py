def is_doubly_linked_palindrome(first):
    '''Checks if a doubly linked list is a palindrome.

    >>> from utils.doubly_linked_list import Node
    >>> is_doubly_linked_palindrome(Node.from_list([1, 2, 3, 1]))
    False
    >>> is_doubly_linked_palindrome(Node.from_list([1, 2, 2, 1]))
    True
    >>> is_doubly_linked_palindrome(Node.from_list([1, 2, 3, 2, 1]))
    True
    >>> is_doubly_linked_palindrome(Node.from_list([1, 2]))
    False
    '''

    # Find last element in linked list and get length
    length = 1
    end = first
    while end.next is not None:
        length += 1
        end = end.next
    begin = first
    for i in range(length // 2):
        if begin.value != end.value:
            return False
        begin, end = begin.next, end.prev
    return True


def is_linked_list_palindrome(first):
    '''Check if a simple linked list is a palindrome.

    Will preserve the linked list:
    >>> from utils.linked_list import Node
    >>> l = Node.from_list([1, 2, 3, 2, 1])
    >>> is_linked_list_palindrome(l)
    True
    >>> l.to_list()
    [1, 2, 3, 2, 1]

    Also works on linked lists with even length.
    >>> is_linked_list_palindrome(Node.from_list([1, 2, 2, 1]))
    True

    And will place back the linked list
    >>> k = Node.from_list([1, 2, 3, 4, 5, 6])
    >>> is_linked_list_palindrome(k)
    False
    >>> k.to_list()
    [1, 2, 3, 4, 5, 6]

    Will also work on edge-cases:
    >>> is_linked_list_palindrome(Node(2))
    True
    >>> is_linked_list_palindrome(Node.from_list([2, 2]))
    True
    >>> is_linked_list_palindrome(Node.from_list([2, 3]))
    False

    Will preserve edge-cases:
    >>> k = Node.from_list([2])
    >>> is_linked_list_palindrome(k)
    True
    >>> k.to_list()
    [2]
    >>> k = Node.from_list([2, 3])
    >>> is_linked_list_palindrome(k)
    False
    >>> k.to_list()
    [2, 3]
    '''
    # Find middle of list (in case of even length, pick last of the two)
    advance_middle = True
    end = middle = first
    while end.next is not None:
        # Only advance middle in half of the cases
        if advance_middle:
            middle = middle.next
        end = end.next
        advance_middle = not advance_middle
    # Reverse starting from middle
    prev, current = None, middle
    while current is not None:
        next = current.next
        current.next = prev
        prev, current = current, next
    # Start comparing from begin and end
    a, b = first, end
    retval = True
    while a is not None and b is not None:
        if a.value != b.value:
            retval = False
            break
        a, b = a.next, b.next
    # Put linked list back to its original state by reversing it again
    prev, current = None, end
    while current is not None:
        next = current.next
        current.next = prev
        prev, current = current, next
    return retval
