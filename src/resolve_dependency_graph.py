from collections import deque


def resolve_dependency_graph(dependency_graph):
    '''Resolves a dependency graph.

    Every entry in the dictionary has a list of dependencies.

    Here, 2 needs 1, and 3 needs both 1 and 2.
    >>> resolve_dependency_graph({3: [1, 2], 2: [1], 1:[]})
    [1, 2, 3]

    If there is a cycle in the graph (i.e. an impossible dependency_graph),
     a ValueError will be thrown.
    >>> resolve_dependency_graph({3: [1, 2], 2: [1], 1: [3]})
    Traceback (most recent call last):
        ...
    ValueError: Cycle detected
    '''
    # This problem is equivalent to :
    #  - transposing a directed graph
    #  - finding a topological ordering of a directed graph

    # Transpose graph
    transposed = {node: [] for node in dependency_graph}
    for node, dependencies in dependency_graph.items():
        for dependency in dependencies:
            transposed[dependency].append(node)

    # Find topological ordering
    # Count number of incoming dependencies
    indegrees = {k: len(v) for k, v in dependency_graph.items()}
    # Queue of nodes with indegree 0 (i.e. items that don't have anything depending on them)
    q = deque(node for node, indegree in indegrees.items() if indegree == 0)
    result = []
    # As long as there are nodes in the queue
    while q:
        new = q.popleft()
        result.append(new)
        # Decrease indegree counter of nodes depending on this node
        for node in transposed[new]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                q.append(node)
        # Delete node from indegrees
        del indegrees[new]
    # Check if there is a cycle
    if len(indegrees) != 0:
        raise ValueError('Cycle detected')
    return result
