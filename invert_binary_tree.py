def invert_binary_tree(root):
    '''Inverts a binary tree given the root node.'''
    # Invert children
    root.left, root.right = root.right, root.left
    # Recursively invert children
    for child in (root.left, root.right):
        if child is not None:
            invert_binary_tree(child)
