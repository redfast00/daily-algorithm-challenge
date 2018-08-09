import numbers
import operator


OPERATORS = {
    '+': operator.add,
    '*': operator.mul,
    '-': operator.sub,
    '/': operator.floordiv
}


def evaluate_reverse_polish(lst):
    '''Evaluates an arithmetic expression in reverse polish notation.

    >>> evaluate_reverse_polish([5, 3, '+'])
    8
    >>> evaluate_reverse_polish([5, 3, 2, '*', '+'])
    11
    >>> evaluate_reverse_polish([5, 2, '-'])
    3
    >>> evaluate_reverse_polish([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'])
    5
    '''
    stack = []
    for element in lst:
        if isinstance(element, numbers.Number):
            stack.append(element)
        else:
            second, first = stack.pop(), stack.pop()
            stack.append(OPERATORS[element](first, second))
    assert len(stack) == 1
    return stack[0]
