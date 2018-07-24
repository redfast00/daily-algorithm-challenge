class PreprocessedSum:
    '''Supports ranged sum queries over a list.

    >>> p = PreprocessedSum([1, 2, 3, 4, 5])
    >>> p.query(0, 5) # 1+2+3+4+5
    15
    >>> p.query(1, 2)
    2
    >>> p.query(1, 1)
    0
    >>> p.query(2, 4)
    7
    '''
    def __init__(self, iterable):
        # Calculates the cumulative sum
        s = [0]
        current_sum = 0
        for number in iterable:
            current_sum += number
            s.append(current_sum)
        self.preprocessed = s

    def query(self, begin, end):
        return self.preprocessed[end] - self.preprocessed[begin]
