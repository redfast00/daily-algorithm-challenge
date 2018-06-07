import random


def toss(chance=0.50):
    return random.random() > chance


def unbiased_toss(tossfunction=toss):
    '''Given a biased cointossfunction, returns a fair coin toss.

    >>> unbiased_toss() in (True, False)
    True
    '''
    first, second = toss(), toss()
    while first == second:
        first, second = toss(), toss()
    return first
