import heapq


def merge_sorted_linked_lists(*nodes):
    '''Merges sorted linked lists into one linked list.
    >>> from utils.linked_list import Node
    >>> first = Node.from_list([1,2,3,5,8])
    >>> second = Node.from_list([2,3,5,6,7,10])
    >>> merge_sorted_linked_lists(first, second).to_list()
    [1, 2, 2, 3, 3, 5, 5, 6, 7, 8, 10]
    '''
    priority_queue = [(node.value, idx, node) for idx, node in enumerate(nodes)]
    heapq.heapify(priority_queue)

    first = get_first_and_update(priority_queue)
    current = first
    while priority_queue:
        node = get_first_and_update(priority_queue)
        current.next = node
        current = node
    return first


def get_first_and_update(priority_queue):
    (value, idx, node) = heapq.heappop(priority_queue)
    new_node = node.next
    if new_node is not None:
        heapq.heappush(priority_queue, (new_node.value, idx, new_node))
    return node
