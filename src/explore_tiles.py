from collections import deque, namedtuple

ExploreItem = namedtuple('ExploreItem', ['coordinates', 'distance'])


def find_path(walls, start_coordinates, end_coordinates):
    '''Finds the length of the shortest path from start_coordinates to end_coordinates.
    >>> t = True; f = False
    >>> find_path([[f, f, f], [f, t, t], [f, f, f]], (2, 2), (0, 2))
    6
    >>> find_path([[f, f, f], [t, t, t], [f, f, f]], (2, 2), (0, 0))
    '''
    to_explore = deque()
    explored = set()
    height = len(walls)
    width = len(walls[0])

    to_explore.append(ExploreItem(start_coordinates, 0))
    while to_explore:
        current = to_explore.popleft()
        if current.coordinates in explored:
            continue
        elif current.coordinates == end_coordinates:
            return current.distance
        else:
            x, y = current.coordinates
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_coordinates = (x + dx, y + dy)
                if (x + dx in range(height)
                        and y + dy in range(width)
                        and not walls[x + dx][y + dy]
                        and new_coordinates not in explored):
                    to_explore.append(ExploreItem(new_coordinates, current.distance + 1))
            explored.add(current.coordinates)
