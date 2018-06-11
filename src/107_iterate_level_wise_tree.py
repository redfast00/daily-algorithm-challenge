from collections import deque


def iterate_level_wise_tree(root):
    '''Iterates level-wise through a binary tree.

    >>> from utils.binary_tree import Node
    >>> list(iterate_level_wise_tree(Node.from_list([1, [2], [3, [4], [5]]])))
    [1, 2, 3, 4, 5]
    '''
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        yield node.value
        for child in (node.left, node.right):
            if child is not None:
                q.append(child)
