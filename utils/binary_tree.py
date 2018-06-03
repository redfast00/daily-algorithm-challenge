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

    def set_left(self, child):
        self.left = child
        child.parent = self
        return self

    def set_right(self, child):
        self.right = child
        child.parent = self
        return self

    def remove_left(self):
        del self.left
        self.left = None

    def remove_right(self):
        del self.right
        self.right = None

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right

    def __repr__(self):
        return f'<{self.__class__.__name__} ({self.value})>)'
