class Node:
    next = prev = None

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_list(cls, lst, head=None, tail=None):
        assert lst
        result = Node(lst[0])
        current = result
        if head is not None:
            head.next = current
            current.prev = head
        for element in lst[1:]:
            new = Node(element)
            current.next = new
            new.prev = current
            current = new
        if tail is not None:
            current.next = tail
            tail.prev = current
        return result

    def to_list(self):
        result = []
        current = self
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'
