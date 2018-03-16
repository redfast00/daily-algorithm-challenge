class Node(object):
    def __init__(self,  value):
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

    def set_next(self, node):
        self.next = node
