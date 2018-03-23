import collections
from utils.linked_list import Node


class NodeQueue(collections.deque):
    def popleft(self, default=None):
        if len(self) > 0:
            return super().popleft()
        else:
            return default


def remove_kth_last_element(linked_list, k):
    '''Removes the k-th last node from a linked list by only iterating over it once.

    >>> linked_list = Node.from_list([1, 5, 8, 60, 82, 64])
    >>> remove_kth_last_element(linked_list, 3).to_list()
    [1, 5, 8, 82, 64]
    >>> linked_list = Node.from_list([1, 2, 8, 5])
    >>> remove_kth_last_element(linked_list, 1).to_list()
    [1, 2, 8]
    >>> linked_list = Node.from_list([1, 2, 8, 5])
    >>> remove_kth_last_element(linked_list, 4).to_list()
    [2, 8, 5]
    >>> linked_list = Node.from_list([1, 2, 5, 8])
    >>> remove_kth_last_element(linked_list, 5).to_list()
    Traceback (most recent call last):
    AssertionError: Linked list doesn't contain enough nodes
    '''

    node_queue = NodeQueue(maxlen=k+1)
    this = linked_list
    while this is not None:
        node_queue.append(this)
        this = this.next
    assert len(node_queue) >= k, f"Linked list doesn't contain enough nodes"
    if len(node_queue) == k + 1:
        # Node before node that should be deleted
        keep_node = node_queue.popleft()
        # Node that should be removed
        node_queue.popleft()
        # Node that keep_node should point to
        pointee_node = node_queue.popleft()
        keep_node.next = pointee_node
    else:
        # Only first node should be deleted
        return linked_list.next
    return linked_list
