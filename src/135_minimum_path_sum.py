from utils import INFINITY


def minimum_path_sum(node):
    '''Finds the minimum path sum of a binary tree.
    >>> from utils.binary_tree import Node
    >>> tree = Node.from_list([10, [5, None, [2]], [5, [1, [-1], None], None]])
    >>> minimum_path_sum(tree)
    (15, [-1, 1, 5, 10])
    '''
    minimum = INFINITY
    minimum_path = None
    if node is None:
        return minimum, minimum_path
    for child in (node.left, node.right):
        total, path = minimum_path_sum(child)
        # Update minimum if child is smaller
        if total < minimum:
            minimum = total
            minimum_path = path
    # If both children are None, and so returned INFINITY, this node is a leaf
    if minimum == INFINITY:
        return node.value, [node.value]
    minimum += node.value
    minimum_path.append(node.value)
    return minimum, minimum_path
