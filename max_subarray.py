from collections import deque


def max_subarray(arr, k):
    '''Returns the max of subarrays of length k in arr.
    >>> max_subarray([10, 5, 2, 7, 8, 7], 3)
    [10, 7, 8, 8]
    '''
    result = []
    queue = deque()
    for i, element in enumerate(arr):
        # Remove old elements from list
        if (queue and queue[0] == i - k):
            queue.popleft()

        # Remove smaller elements
        while queue and arr[queue[-1]] < element:
            queue.pop()

        # Add current element
        queue.append(i)
        if i >= k - 1:
            result.append(arr[queue[0]])
    return result
