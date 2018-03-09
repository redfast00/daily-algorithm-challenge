def longest_distinct_substring(s, k):
    '''Returns the length of the longest substring containing at most k characters.
    Runs in O(k*n) time, and in O(k) space
    >>> longest_distinct_substring('abcba', 2)
    3
    >>> longest_distinct_substring('abcdef', 2)
    2
    >>> longest_distinct_substring('aaaa', 2)
    4
    >>> longest_distinct_substring('aaaab', 1)
    4
    >>> longest_distinct_substring('aaabcdeeee', 1)
    4
    >>> longest_distinct_substring('test', 58)
    4
    '''
    last_seen = {}
    begin = -1
    max_ = 0
    # Loops over each character, costs n time
    for idx, char in enumerate(s):
        if char in last_seen:
            last_seen[char] = idx
        else:
            if len(last_seen) < k:
                last_seen[char] = idx
            else:
                # find minimum, costs k time
                to_remove_key = min(last_seen, key=last_seen.get)
                begin = last_seen[to_remove_key]
                del last_seen[to_remove_key]
                last_seen[char] = idx
        max_ = max(max_, idx - begin)
    return max_
