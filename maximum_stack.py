class MaximumStack:
    '''Implementation of a stack where push, pop and max run in O(1) time.

    >>> s = MaximumStack()
    >>> s.max() is None
    True
    >>> s.push(20)
    >>> s.max()
    20
    >>> s.push(30)
    >>> s.max()
    30
    >>> s.pop()
    30
    >>> s.max()
    20
    '''
    def __init__(self):
        self.stack = []
        self.maximum = None

    def push(self, item):
        self.stack.append((item, self.maximum))
        if self.maximum is None:
            self.maximum = item
        else:
            self.maximum = max(self.maximum, item)

    def pop(self):
        item, maximum = self.stack.pop()
        self.maximum = maximum
        return item

    def max(self):
        return self.maximum
