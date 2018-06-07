def deepest_node(root):
    '''Returns the deepest node in a binary tree.
    >>> from utils.binary_tree import Node
    >>> deepest_node(Node.from_list([1])).value
    1
    >>> deepest_node(Node.from_list([1, [2], [3, [8], None]])).value
    8
    '''
    deepest, _ = deepest_node_recursive(root)
    return deepest


def deepest_node_recursive(root):
    level = 0
    current = root
    for child in (root.left, root.right):
        if child is not None:
            max_node, max_level = deepest_node_recursive(child)
            if level < max_level:
                current, level = max_node, max_level
    return current, level + 1
