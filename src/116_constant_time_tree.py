class Node:
    '''Generate a binary tree of arbitrarily large, but finite size in constant time.'''
    def __init__(self, value):
        self.value = value

    @property
    def left(self):
        if self.value > 0:
            return self.__class__(self.value - 1)
        return None

    @property
    def right(self):
        if self.value > 0:
            return self.__class__(self.value - 1)
        return None
