class SparseList:
    '''A list where most values are the same.
    >>> l = SparseList([1, 0, 0, 2, 0, 0])
    >>> l[0]
    1
    >>> l[1]
    0
    >>> l[0] = 2
    >>> l[0]
    2
    >>> l[0] = 0
    >>> l[0]
    0

    '''
    def __init__(self, original, common=0):
        self.common = common
        self.uncommon = {}
        for key, value in enumerate(original):
            self[key] = value

    def __getitem__(self, idx):
        return self.uncommon.get(idx, self.common)

    def __setitem__(self, idx, value):
        if value == self.common and idx in self.uncommon:
            del self.uncommon[idx]
        self.uncommon[idx] = value
