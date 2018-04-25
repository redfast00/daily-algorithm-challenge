from collections import OrderedDict, defaultdict


class OrderedDefaultDict(OrderedDict):
    def __missing__(self, key):
        self[key] = value = 0
        return value


class FlightStorage():
    amount = 0

    def __init__(self):
        self.storage = defaultdict(OrderedDefaultDict)

    def add(self, start, destination):
        self.storage[start][destination] += 1
        self.amount += 1

    def list(self, start):
        return (destination for destination, amount in self.storage[start].items() if amount > 0)

    def remove(self, start, destination):
        self.storage[start][destination] -= 1
        self.amount -= 1

    def __len__(self):
        return self.amount


def reassemble_flights(start, flights):
    '''Reassembles a series of flights.

    >>> reassemble_flights('YUL', [('YUL', 'SFO'), ('SFO', 'HKO')])
    ['YUL', 'SFO', 'HKO']
    >>> reassemble_flights('YUL', [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')])
    ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

    Returns the first (alphabetically sorted) route:
    >>> reassemble_flights('A', [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')])
    ['A', 'B', 'C', 'A', 'C']

    If no solution is available, returns None:
    >>> reassemble_flights('COM', [('SFO', 'COM'), ('COM', 'YYZ')]) is None
    True
    '''
    storage = FlightStorage()
    for flight in sorted(flights):
        storage.add(*flight)
    return backtrack_flights(start, storage)


def backtrack_flights(start, storage):
    if len(storage) == 0:
        return [start]
    if not any(storage.list(start)):
        return
    for destination in storage.list(start):
        storage.remove(start, destination)
        result = backtrack_flights(destination, storage)
        if result is not None:
            return [start] + result
        storage.add(start, destination)
