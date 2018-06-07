import heapq


def get_second_largest_node(root):
    '''Gets the second largest node from a binary tree.

    >>> from utils.binary_tree import Node
    >>> tree = Node.from_list([1, None, [2, [3], [5, [8], [60]]]])
    >>> get_second_largest_node(tree).value
    8
    >>> tree = Node.from_list([3, None, [2, [3], [5, [8], [3]]]])
    >>> get_second_largest_node(tree).value
    5
    '''
    _, second = get_two(root)
    assert second is not None, "Not enough values"
    return second


def get_two(root):
    result = [root]
    if root.left is not None:
        result.extend(get_two(root.left))
    if root.right is not None:
        result.extend(get_two(root.right))
    return heapq.nlargest(2, result, key=lambda node: node.value)
