class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
        return self
