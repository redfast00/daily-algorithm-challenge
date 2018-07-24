def prune_tree(root):
    '''Prunes all subtrees only containing zero.
    >>> from utils.binary_tree import Node
    >>> tree = Node.from_list_representation([0, 1, 0, None, None, 1, 0, None, None, None, None, 0, 0])
    >>> tree = prune_tree(tree)
    >>> tree == Node.from_list_representation([0, 1, 0, None, None, 1])
    True
    '''
    if root is None:
        return None
    root.left = prune_tree(root.left)
    root.right = prune_tree(root.right)
    # Base case
    if root.left is None and root.right is None and root.value == 0:
        return None
    return root
