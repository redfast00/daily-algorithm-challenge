def min_rooms_required(intervals):
    '''Returns the minimum amount of rooms necessary.

    Input consists of a list of time-intervals (start, stop):
    >>> min_rooms_required([(10, 20), (15, 25)])
    2
    >>> min_rooms_required([(10, 20), (20, 30)])
    1
    '''
    # transform intervals
    # [(10, 20), (15, 25)]
    # to
    # [(10, 1), (15, 1), (20, -1), (25, -1)]
    times = []
    for interval in intervals:
        start, stop = interval
        assert start < stop
        times.append((start, 1))
        times.append((stop, -1))
    times.sort()

    rooms_required = 0
    current_rooms_taken = 0
    for _, status in times:
        current_rooms_taken += status
        rooms_required = max(current_rooms_taken, rooms_required)
    return rooms_required
