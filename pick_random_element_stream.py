import collections
import random


def pick_random_element(iterable):
    '''Picks a random element from a stream that might not fit into memory.
    >>> pick_random_element([123])
    123
    '''
    picked = None
    for idx, element in enumerate(iterable):
        if random.random() < (1 / (idx + 1)):
            picked = element
    return picked


def get_distribution(iterable, trials=10000):
    distibution = collections.defaultdict(lambda: 0)
    for _ in range(trials):
        element = pick_random_element(iterable)
        distibution[element] += 1
    return distibution
