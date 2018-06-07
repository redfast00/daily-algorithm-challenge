operations = {
    '+': (lambda x, y: x + y),
    '/': (lambda x, y: x / y),
    '*': (lambda x, y: x * y),
    '-': (lambda x, y: x - y)
}


def evaluate(root):
    '''Evaluates a binary tree.

    >>> from utils.binary_tree import Node
    >>> tree = Node.from_list(['*',
    ... ['+', ['3'], ['2']],
    ... ['+', ['4'], ['5']]])
    >>> evaluate(tree)
    45
    '''
    # Base case
    if root.value.isdigit():
        return int(root.value)
    # Check if operation is supported
    assert root.value in operations, f'Unsupported operation: {root.value}'
    assert root.left is not None, "Left child required"
    assert root.right is not None, "Right child required"
    op = operations[root.value]
    return op(evaluate(root.left), evaluate(root.right))
