''' Autocomplete a word to words in a dictionary
>>> d = {"first", "example", "test", "tester", "", "fi"}
>>> preprocessed = preprocess(d)
>>> complete("ex", preprocessed) == {"example"} # dirty fix for doctest
True
>>> complete("test", preprocessed) == {"test", "tester"}
True
>>> complete("f", preprocessed) == {"first", "fi"}
True
>>> complete("extra", preprocessed) == set()
True
>>> complete("q", preprocessed) == set()
True
'''

from collections import defaultdict


class LetterTree(defaultdict):
    exists = False


def Tree(): return LetterTree(Tree)


def preprocess(dictionary_set):
    t = Tree()
    for word in dictionary_set:
        root = t
        for letter in word:
            root = root[letter]
        root.exists = True
    return t


def complete(part, preprocessed_dict):
    results = set()
    root = preprocessed_dict
    for letter in part:
        if letter not in root:
            # This will empty
            return results
        else:
            root = root[letter]
    for subresult in walk(root):
        results.add(part + subresult)
    return results


def walk(root):
    if root.exists:
        yield ''
    for key in root:
        subtree = root[key]
        for result in walk(subtree):
            yield key + result
