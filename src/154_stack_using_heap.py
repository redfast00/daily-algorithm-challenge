import heapq


class Stack:
    '''A stack implementation using a heap

    >>> a = Stack()
    >>> a.push(2)
    >>> a.push(1)
    >>> a.push(3)
    >>> a.pop()
    3
    >>> a.push(4)
    >>> a.pop()
    4
    >>> a.pop(), a.pop()
    (1, 2)
    '''
    def __init__(self):
        self.heap = []
        self.curval = 0

    def push(self, item):
        heapq.heappush(self.heap, (self.curval, item))
        self.curval -= 1

    def pop(self):
        if not self.heap:
            raise IndexError('pop from empty stack')
        return heapq.heappop(self.heap)[1]
