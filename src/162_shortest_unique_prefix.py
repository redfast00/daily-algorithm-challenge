from collections import defaultdict
from enum import Enum


class NodeState(Enum):
    EMPTY = 0
    ONE = 1
    MANY = 2


class Node:
    def __init__(self):
        self.value = None
        self.state = NodeState.EMPTY
        self.letters = defaultdict(Node)

    def add(self, word):
        if word == '':
            raise ValueError('Impossible to find unique prefix')
        if self.state == NodeState.EMPTY:
            self.value = word
            self.state = NodeState.ONE
        elif self.state == NodeState.ONE:
            self.letters[self.value[0]].add(self.value[1:])
            self.letters[word[0]].add(word[1:])
            self.value = None
            self.state = NodeState.MANY
        else:
            self.letters[word[0]].add(word[1:])

    def get_prefix(self, word):
        if self.value == word:
            return ''
        assert word[0] in self.letters, 'Word not found'
        return word[0] + self.letters[word[0]].get_prefix(word[1:])


def shortest_unique_prefix(words):
    '''Finds the shortest unique prefix for the given words.

    >>> shortest_unique_prefix(['dog', 'cat', 'apricot', 'apple', 'fish'])
    ['d', 'c', 'apr', 'app', 'f']
    >>> shortest_unique_prefix(['dog', 'dogfood'])
    Traceback (most recent call last):
    ValueError: Impossible to find unique prefix
    '''
    t = Node()
    for word in words:
        t.add(word)
    return [t.get_prefix(word) for word in words]
