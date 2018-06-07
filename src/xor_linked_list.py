class RawMemory(object):
    '''Represents raw memory.'''
    def __init__(self):
        self._pointer_to_object = {}
        self._object_to_pointer = {}
        # address 0 won't be used
        self._current_pointer = 0

    def get_pointer(self, obj):
        assert obj in self._object_to_pointer
        return self._object_to_pointer[obj]

    def dereference_pointer(self, pointer):
        assert pointer in self._pointer_to_object
        return self._pointer_to_object[pointer]

    def allocate(self, obj):
        new_pointer = self._current_pointer + 1
        self._current_pointer = new_pointer
        self._pointer_to_object[new_pointer] = obj
        self._object_to_pointer[obj] = new_pointer
        return new_pointer


class Node(object):
    def __init__(self, value):
        self.value = value
        self.both = 0


class XORLinkedList(object):
    '''Compact double-linked list.
    >>> l = XORLinkedList()
    >>> l.add(5)
    >>> l.add(8)
    >>> l.add(50)
    >>> l.add(23)
    >>> l.get(0)
    5
    >>> l.get(1)
    8
    >>> l.get(2)
    50
    >>> l.get(3)
    23
    '''
    def __init__(self):
        self.mem = RawMemory()
        self.begin_node_pointer = 0
        self.amount = 0

    def add(self, element):
        # instead of inserting at the end, we insert at the beginning and change the get function
        new_node = Node(element)
        new_node_pointer = self.mem.allocate(new_node)
        if self.begin_node_pointer != 0:
            old_node = self.mem.dereference_pointer(self.begin_node_pointer)
            # old_node.both is the following node xor'd with 0, and a ^ 0 = a
            old_node.both = old_node.both ^ new_node_pointer
            new_node.both = self.begin_node_pointer ^ 0
        self.begin_node_pointer = new_node_pointer
        self.amount += 1

    def get(self, index):
        assert index in range(self.amount), "Index not in linked list"
        # instead of inserting at the end, we insert at the beginning and change the get function
        index = self.amount - index - 1
        previous_pointer = 0
        current_pointer = self.begin_node_pointer
        for _ in range(index):
            next_pointer = self.mem.dereference_pointer(current_pointer).both ^ previous_pointer
            previous_pointer, current_pointer = (current_pointer, next_pointer)
        return self.mem.dereference_pointer(current_pointer).value
