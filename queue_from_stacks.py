class Queue:
    '''A queue implementation using two stacks.
    >>> q = Queue()
    >>> len(q)
    0
    >>> q.enqueue(5)
    >>> len(q)
    1
    >>> q.enqueue(6)
    >>> q.dequeue()
    5
    >>> q.dequeue()
    6
    '''
    def __init__(self):
        self.popstack = []
        self.pushstack = []

    def enqueue(self, item):
        self.pushstack.append(item)

    def dequeue(self):
        if not self.popstack:
            while self.pushstack:
                self.popstack.append(self.pushstack.pop())
        assert self.popstack, "no item in queue"
        return self.popstack.pop()

    def __len__(self):
        return len(self.popstack) + len(self.pushstack)
