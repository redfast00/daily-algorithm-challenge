from collections import Counter


def is_permutation_palindrome(s):
    '''Determines if a permutation of a string is a palindrome.

    >>> is_permutation_palindrome('carrace') # racecar
    True
    >>> is_permutation_palindrome('abcd')
    False
    >>> is_permutation_palindrome('daily')
    False
    '''
    count = Counter(s)
    used_odd_amount = False
    # Each character should appear an even amount of times in the string, except
    #  possibly the middle character.
    for amount in count.values():
        if amount % 2 == 1:
            if used_odd_amount:
                return False
            used_odd_amount = True
    return True
