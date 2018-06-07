from utils.binary_tree import Node

def serialize(rootnode):
    if rootnode is None:
        return ''
    return f'{rootnode.value}<{serialize(rootnode.left)},{serialize(rootnode.right)}>'

def deserialize(serialized):
    accumulator = None
    result = Node()
    current_node = result
    for char in serialized:
        if char.isdigit():
            if accumulator is None:
                accumulator = 0
            accumulator *= 10
            accumulator += int(char)
        elif char == '<':
            current_node.value = accumulator
            accumulator = None
            left_node = Node()
            current_node.set_left(left_node)
            current_node = left_node
        elif char == ',':
            current_node = current_node.parent
            if current_node.left.value is None:
                current_node.remove_left()
            right_node = Node()
            current_node.set_right(right_node)
            current_node = right_node
        elif char == '>':
            current_node = current_node.parent
            if current_node.right.value is None:
                current_node.remove_right()
    return result
if __name__ == "__main__":
    root = Node(5).set_left(Node(4).set_right(Node(8))).set_right(Node(21))
    d = deserialize(serialize(root))
    assert d == root
