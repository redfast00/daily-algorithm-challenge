def cons(a, b):
    return lambda f: f(a, b)

def car(pair):
    '''Returns first element of pair.
    >>> car(cons(1, 8))
    1
    '''
    f = lambda a, b: a
    return pair(f)

def cdr(pair):
    '''Returns second element of pair.
    >>> cdr(cons(1, 8))
    8
    '''
    f = lambda a, b: b
    return pair(f)
