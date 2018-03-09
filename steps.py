from functools import lru_cache


# Purpose: this class is hashable, and so the recursive_counter function can be cached
class StepSizes(list):
    def __hash__(self):
        return hash(frozenset(self))


def count_steps(step_sizes, staircase_length):
    '''Counts the possible ways to go down a staircase with steps of size possible_lengths
    >>> count_steps({1, 2}, 3)
    3
    >>> count_steps({1, 2}, 4)
    5
    >>> count_steps({5, 6}, 2)
    0
    '''
    lst = StepSizes(sorted(step_sizes))
    return recursive_counter(lst, staircase_length)


@lru_cache(maxsize=2**10)
def recursive_counter(possible_lengths, staircase_length):
    print(staircase_length)
    # expects an ordered possible_lengths
    total_ways = 0
    for stepsize in possible_lengths:
        if stepsize < staircase_length:
            total_ways += recursive_counter(possible_lengths, staircase_length - stepsize)
        elif stepsize == staircase_length:
            return total_ways + 1
        else:
            return total_ways
    return total_ways
