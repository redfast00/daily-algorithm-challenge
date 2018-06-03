from utils import INFINITY


def testhelper(root):
    node, size = find_largest_BST(root)
    return node.value, size


def find_largest_BST(root):
    '''
    Returns the largest subtree that is a valid binary search tree and
    the amount of nodes in it.

    >>> from utils.binary_tree import Node
    >>> testhelper(Node.from_list([1]))
    (1, 1)
    >>> testhelper(Node.from_list([1, [0], [2]]))
    (1, 3)
    >>> testhelper(Node.from_list([1, [3], [2, [1], [5]]]))
    (2, 3)
    >>> testhelper(Node.from_list([1, [0, [-1], [3]], [2]]))
    (0, 3)
    '''
    size, _, largest, _, _ = largest_BST_recursive(root)
    return largest, size


def largest_BST_recursive(node):
    if node is None:
        # BST has size: 0 nodes, BST is valid, there is no largest BST node
        return 0, True, None, INFINITY, -INFINITY
    size_left, valid_left, largest_left, _, max_left = largest_BST_recursive(node.left)
    size_right, valid_right, largest_right, min_right, _ = largest_BST_recursive(node.right)
    # Check if this node is a valid BST
    if max_left < node.value < min_right and valid_left and valid_right:
        this_min = node.value if max_left == -INFINITY else max_left
        this_max = node.value if min_right == INFINITY else min_right
        return size_left + size_right + 1, True, node, this_min, this_max
    # This node is invalid, propagate largest node
    largest_node = largest_left if size_left > size_right else largest_right
    return max(size_left, size_right), False, largest_node, -INFINITY, INFINITY
