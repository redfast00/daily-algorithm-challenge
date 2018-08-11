import random


def random_weighted_probability(values, weights):
    assert len(values) == len(weights)
    generated = random.random()
    cumsum = 0
    for index, weight in enumerate(weights):
        cumsum += weight
        if generated < cumsum:
            return values[index]
    raise ValueError('weights do not have a sum of 1')
