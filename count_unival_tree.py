from tree import Node


def count_unival_subtrees(root):
    '''Count unival trees.
    >>> tree = Node(5).add_child(Node(5)).add_child(Node(5))
    >>> count_unival_subtrees(tree)
    3
    >>> tree = Node(1).add_child(Node(1)).add_child(Node(2)).add_child(Node(2))
    >>> count_unival_subtrees(tree)
    3
    '''
    if not root.children:
        return 1
    else:
        return sum((count_unival_subtrees(child) for child in root.children)) + is_unival_tree(root)


def is_unival_tree(root):
    # Check if all values of child nodes are equal to own value
    for child in root.children:
        if child.value != root.value:
            return False
    # Check if all children are unival trees
    return all((is_unival_tree(child) for child in root.children))
