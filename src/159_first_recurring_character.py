def first_recurring_character(s):
    '''Returns the first recurring character, or None if all characters are unique.

    >>> first_recurring_character('test')
    't'
    >>> first_recurring_character('') is None
    True
    >>> first_recurring_character('abcd') is None
    True
    >>> first_recurring_character('abcbcccc')
    'b'
    '''
    found = set()
    for char in s:
        if char in found:
            return char
        found.add(char)
    return None
