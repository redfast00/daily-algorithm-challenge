class Node(object):
    def __init__(self, value=None):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def set_left(self, child):
        self.left = child
        child.parent = self
        return self

    def set_right(self, child):
        self.right = child
        child.parent = self
        return self

    def remove_left(self):
        del self.left
        self.left = None

    def remove_right(self):
        del self.right
        self.right = None

    def __eq__(self, other):
        return self.value == other.value and self.left == other.left and self.right == other.right
