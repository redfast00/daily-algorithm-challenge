class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    @classmethod
    def from_list(cls, lst, end=None):
        assert lst
        result = Node(lst[0])
        current = result
        for element in lst[1:]:
            new = Node(element)
            current.set_next(new)
            current = new
        current.set_next(end)
        return result

    def to_list(self):
        result = []
        this = self
        seen = set()
        while this is not None:
            if this in seen:
                raise ValueError('Circular linked list detected')
            seen.add(this)
            result.append(this.value)
            this = this.next
        return result

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'
