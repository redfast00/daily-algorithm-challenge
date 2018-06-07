def is_matched(to_check, brackets=('{}', '()', '[]')):
    '''Checks if a string consisting of brackets is matched.

    >>> is_matched('({}[])')
    True
    >>> is_matched('(({))')
    False
    >>> is_matched('((')
    False
    '''
    stack = []
    matched = {s[1]: s[0] for s in brackets}
    for char in to_check:
        if char in matched:
            matching_bracket = matched[char]
            # char is a closing bracket, check if open bracket is on stack
            if len(stack) == 0 or stack.pop() != matching_bracket:
                return False
        else:
            stack.append(char)
    return len(stack) == 0
