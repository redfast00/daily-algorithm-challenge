import itertools
import operator


def paint_cost(costmatrix):
    '''Paints len(costmatrix) houses in len(costmatrix[0]) different colors.
    costmatrix[n][k] is the cost to paint the n'th house in the k'th color.
    No two neighbouring houses can have the same problem.
    >>> paint_cost([[1, 2, 8], [5, 6, 2], [1, 20, 2]])
    4
    '''
    n = len(costmatrix)
    current_costs = list(costmatrix[0])
    for i in range(1, n):
        current_costs = list(map(operator.add, costmatrix[i], minima_excluding_self(current_costs)))
    return min(current_costs)


def minima_excluding_self(costs):
    '''Calculates the cost of painting previous houses in a color.
    >>> minima_excluding_self([4, 3, 8, 7])
    [3, 4, 3, 3]
    >>> minima_excluding_self([1, 2])
    [2, 1]
    '''
    min_idx = min(range(len(costs)), key=lambda x: costs[x])
    result = [costs[min_idx]] * len(costs)
    second_min_idx = min(
        itertools.chain(range(min_idx), range(min_idx + 1, len(costs))),
        key=lambda x: costs[x])
    result[min_idx] = costs[second_min_idx]
    return result
