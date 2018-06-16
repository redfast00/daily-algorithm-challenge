class Node(object):
    def __init__(self, value=None):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    @classmethod
    def from_list(cls, lst):
        '''Returns a binary tree made from nested lists.

        The first item in the list is the value of the Node.
        The second item is the left child.
        The third item is the right child.
        For example:
        [1, None, [2, [3], None]]
        '''
        result = cls(lst[0])
        if len(lst) == 1:
            return result
        if lst[1] is not None:
            result.set_left(cls.from_list(lst[1]))
        if lst[2] is not None:
            result.set_right(cls.from_list(lst[2]))
        return result

    @classmethod
    def from_list_representation(cls, lst, current=0):
        '''Returns a binary tree made from the list representation of itself.

        Suppose list indexes start from 1, then every node has it children at
        2 * index and at 2 * index + 1.
        >>> (Node.from_list([1, None, [2, [3], [4]]])
        ...  == Node.from_list_representation([1, None, 2, None, None, 3, 4]))
        True
        '''
        if current not in range(len(lst)) or lst[current] is None:
            return None
        result = cls(lst[current])
        result.set_left(cls.from_list_representation(lst, current=2*current+1))
        result.set_right(cls.from_list_representation(lst, current=2*current+2))
        return result

    def set_left(self, child):
        if self.left is not None:
            self.left.parent = None
        self.left = child
        if child is not None:
            child.parent = self
        return self

    def set_right(self, child):
        if self.right is not None:
            self.right.parent = None
        self.right = child
        if child is not None:
            child.parent = self
        return self

    def remove_left(self):
        self.set_left(None)

    def remove_right(self):
        self.set_right(None)

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __repr__(self):
        return f'<{self.__class__.__name__} ({self.value})>)'
