from utils.binary_tree import Node


class LockableNode(Node):
    '''Represents a node in a binary tree.

    >>> bottom = LockableNode(5)
    >>> bottom.is_locked()
    False
    >>> middle = LockableNode(10)
    >>> top = LockableNode(20).set_left(middle.set_right(bottom))
    >>> bottom.lock()
    True
    >>> bottom.is_locked()
    True
    >>> middle.is_locked()
    False
    >>> top.lock()
    True
    >>> middle.lock()
    False
    >>> middle.is_locked()
    False
    >>> bottom.unlock()
    True
    >>> bottom.is_locked()
    False
    >>> middle.lock()
    True
    '''

    def __init__(self, *args, **kwargs):
        self._locked = False
        self._lock_amount = 0
        super().__init__(*args, **kwargs)

    def is_locked(self):
        return self._locked

    def lock(self):
        '''Locks the node and returns whether it succeeded.

        Only succeeds if all ancestor nodes or all descendant nodes are unlocked.
        '''
        if not self._locked and (self._lock_amount == 0 or self._ancestors_unlocked()):
            # lock current node
            self._locked = True
            root = self.parent
            while root is not None:
                root._lock_amount += 1
                root = root.parent
            return True
        else:
            return False

    def unlock(self):
        '''Unlocks the node and returns whether it succeeded.

        Only succeeds if all ancestor nodes or all descendant nodes are unlocked.
        '''
        if self._locked and (self._lock_amount == 0 or self._ancestors_unlocked()):
            # unlock current node
            self._locked = False
            root = self.parent
            while root is not None:
                root._lock_amount -= 1
                root = root.parent
            return True
        else:
            return False

    def _ancestors_unlocked(self):
        root = self.parent
        while root is not None:
            if root.is_locked():
                return False
            root = root.parent
        return True
