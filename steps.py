from functools import lru_cache


def count_steps(step_sizes, staircase_length):
    '''Counts the possible ways to go down a staircase with steps of size possible_lengths
    >>> count_steps({1, 2}, 3)
    3
    >>> count_steps({1, 2}, 4)
    5
    >>> count_steps({5, 6}, 2)
    0
    '''
    # convert to tuple so that recursive_counter can be cached
    lst = tuple(sorted(step_sizes))
    return recursive_counter(lst, staircase_length)


@lru_cache(maxsize=2**10)
def recursive_counter(step_sizes, staircase_length):
    # expects an ordered possible_lengths
    total_ways = 0
    for stepsize in step_sizes:
        if stepsize < staircase_length:
            total_ways += recursive_counter(step_sizes, staircase_length - stepsize)
        elif stepsize == staircase_length:
            return total_ways + 1
        else:
            return total_ways
    return total_ways
