class TwoDimensionalIterator:
    '''A 2D iterator over a lists of lists

    >>> a = TwoDimensionalIterator([[1], [2, 3], [], [4, 5]])
    >>> list(a)
    [1, 2, 3, 4, 5]
    >>> list(TwoDimensionalIterator([[], [], [], [1]]))
    [1]
    '''
    def __init__(self, array):
        self.array = array
        self.first = 0
        self.second = 0

    def __next__(self):
        while self.first < len(self.array) and self.second >= len(self.array[self.first]):
            self.first += 1
            self.second = 0
        if self.first >= len(self.array):
            raise StopIteration()
        self.second += 1
        return self.array[self.first][self.second - 1]

    def __iter__(self):
        return self
