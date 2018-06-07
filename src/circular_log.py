class Logger(object):
    '''Circular log
    >>> l = Logger(5)
    >>> for i in range(5):
    ...     l.record(i)
    >>> l.get_last(1)
    4
    >>> l.get_last(2)
    3
    >>> l.get_last(5)
    0
    >>> l = Logger(3)
    >>> for i in range(30):
    ...     l.record(i)
    >>> l.get_last(1)
    29
    >>> l.get_last(2)
    28
    >>> l.get_last(3)
    27
    '''
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
        self.current_pos = 0

    def record(self, order_id):
        self.data[self.current_pos] = order_id
        self.current_pos = (self.current_pos + 1) % self.size

    def get_last(self, i):
        return self.data[(self.current_pos - i) % self.size]
