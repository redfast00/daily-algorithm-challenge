def check_valid(root):
    '''Checks the validity of a binary seach tree given a root node.
    >>> from utils.binary_tree import Node
    >>> check_valid(Node.from_list([1]))
    True
    >>> check_valid(Node.from_list([1, [0], [2]]))
    True
    >>> check_valid(Node.from_list([1, [3], [2]]))
    False
    '''
    valid, _, _ = check_recursive(root)
    return valid


def check_recursive(root):
    '''Returns if this subtree is valid, the minimum value and the maximum value in it'''
    this_min = this_max = root.value
    if root.left is not None:
        valid, min_left, max_left = check_recursive(root.left)
        if not valid or max_left > root.value:
            return False, None, None
        this_min = min_left
    if root.right is not None:
        valid, min_right, max_right = check_recursive(root.right)
        if not valid or min_right < root.value:
            return False, None, None
        this_max = max_right
    return True, this_min, this_max
