from itertools import islice


def shortest_path(locations):
    '''Finds lenght of the shortest path between a list of 2D coordinates.

    We can move diagonally.
    >>> shortest_path([(0, 0), (1, 1)])
    1
    >>> shortest_path([(0, 0), (1, 1), (1, 2)])
    2
    >>> shortest_path([(0,0), (5, 2)])
    5
    '''
    total = 0
    for first, second in zip(locations, islice(locations, 1, len(locations))):
        dx = abs(first[0] - second[0])
        dy = abs(first[1] - second[1])
        total += max(dx, dy)
    return total
