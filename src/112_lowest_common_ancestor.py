def path_to_root(node):
    path = []
    while node is not None:
        path.append(node)
        node = node.parent
    return path


def lowest_common_ancestor(first, second):
    '''Finds the lowest common ancestor of two nodes in a binary tree.

    >>> from utils.binary_tree import Node
    >>> tree = Node.from_list_representation(list(range(2**5 - 1)))
    >>> lowest_common_ancestor(tree.left.left, tree.left.right) is tree.left
    True
    >>> lowest_common_ancestor(tree, tree.left.right) is tree
    True
    >>> lowest_common_ancestor(tree.left.left.right.left, tree.left.right.left) is tree.left
    True
    '''
    first_path = path_to_root(first)
    second_path = path_to_root(second)
    common_parent = None
    for first_parent, second_parent in zip(reversed(first_path), reversed(second_path)):
        if first_parent is not second_parent:
            return common_parent
        common_parent = first_parent
    return common_parent
