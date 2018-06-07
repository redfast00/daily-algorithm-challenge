from collections import Counter
from get_subset_sum import subset_sum


def partition_into_equal_parts(l):
    '''Partitions s into two subsets of l that have the same sum.

    >>> problem = [15, 5, 20, 10, 35, 25, 10]
    >>> first, second = partition_into_equal_parts(problem)
    >>> valid_solution(first, second, problem)
    True
    '''
    total = sum(l)
    # If sum is odd, there is no way that total = sum(first) + sum(second) = 2 * sum(first)
    if total % 2:
        return
    first = subset_sum(total // 2, l)
    if first is None:
        return
    second = []
    # Fill second with items from counter
    second_counter = Counter(l) - Counter(first)
    for number, amount in second_counter.items():
        second.extend([number] * amount)
    return first, second


def valid_solution(first, second, problem):
    return sum(first) == sum(second) and Counter(first) + Counter(second) == Counter(problem)
