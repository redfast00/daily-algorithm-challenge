from collections import defaultdict


def find_concatenated_palindromes(lst):
    '''Finds indices in the list of strings that when concatenated form a palindrome.

    For example:
    Since 'codeedoc' and 'edoccode' are both palindromes:
    >>> find_concatenated_palindromes(['code', 'edoc'])
    [(0, 1), (1, 0)]
    >>> find_concatenated_palindromes(['da', 'd'])
    [(0, 1)]
    >>> find_concatenated_palindromes(['d', 'da'])
    [(1, 0)]
    >>> find_concatenated_palindromes(['ad', 'd'])
    [(1, 0)]
    >>> find_concatenated_palindromes(['code', 'edoc', 'da', 'd'])
    [(0, 1), (1, 0), (2, 3)]

    This even works with multiple palindromes:
    >>> find_concatenated_palindromes(['da', 'd', 'dq', 'd'])
    [(0, 1), (0, 3), (1, 3), (2, 1), (2, 3), (3, 1)]
    '''
    # For combinations like 'code' 'edoc'
    regular_seen = defaultdict(list)
    # Words with first/last letter chopped off
    chopped_left_seen = defaultdict(list)
    chopped_right_seen = defaultdict(list)

    result = []
    for idx, word in enumerate(lst):
        reversed_word = word[::-1]
        chopped_left = word[1:]
        chopped_right = word[:-1]
        if reversed_word in regular_seen:
            for other_idx in regular_seen[reversed_word]:
                result.extend([(idx, other_idx), (other_idx, idx)])

        if reversed_word in chopped_left_seen:
            for other_idx in chopped_left_seen[reversed_word]:
                result.append((idx, other_idx))

        if reversed_word in chopped_right_seen:
            for other_idx in chopped_right_seen[reversed_word]:
                result.append((other_idx, idx))

        if chopped_left[::-1] in regular_seen:
            for other_idx in regular_seen[chopped_left[::-1]]:
                result.append((other_idx, idx))

        if chopped_right[::-1] in regular_seen:
            for other_idx in regular_seen[chopped_right[::-1]]:
                result.append((idx, other_idx))

        # Update dictionaries
        regular_seen[word].append(idx)
        chopped_left_seen[chopped_left].append(idx)
        chopped_right_seen[chopped_right].append(idx)

    return sorted(result)
