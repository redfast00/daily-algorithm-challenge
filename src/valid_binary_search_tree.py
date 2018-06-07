from utils import INFINITY


def is_valid_BST(root, lowerbound=-INFINITY, upperbound=INFINITY):
    '''Checks the validity of a binary seach tree given a root node.
    >>> from utils.binary_tree import Node
    >>> is_valid_BST(Node.from_list([1]))
    True
    >>> is_valid_BST(Node.from_list([1, [0], [2]]))
    True
    >>> is_valid_BST(Node.from_list([1, [3], [2]]))
    False
    '''
    # Base case
    if root is None:
        return True
    # Check if this node is correct
    if root.value < lowerbound or root.value > upperbound:
        return False
    # Check if children are correct
    return (is_valid_BST(root.left, lowerbound, root.value) and
            is_valid_BST(root.right, root.value, upperbound))
