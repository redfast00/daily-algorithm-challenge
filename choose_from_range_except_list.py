import random


def choose_from_range_except_list(n, not_allowed):
    '''Randomly picks a number between 0 and n (exclusive) that is not in not_allowed.'''
    not_allowed = set(number for number in not_allowed if number in range(n))
    result = random.randrange(n)
    while result in not_allowed:
        result = random.randrange(n)
    return result


def choose_from_range_except_list2(n, not_allowed, amount):
    # Algorithm is more efficient (amortized constant time) when amount gets larger
    allowed = tuple(set(range(n)) - set(not_allowed))
    return [random.choice(allowed) for _ in range(amount)]
