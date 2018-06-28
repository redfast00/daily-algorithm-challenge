import re


def validate_number(s):
    '''Checks if the string is a valid number.

    >>> validate_number('123')
    True
    >>> validate_number('-12')
    True
    >>> validate_number('0')
    True
    >>> validate_number('0.23')
    True
    >>> validate_number('-123.456')
    True

    Also works with exponential notation:
    >>> validate_number('12e3')
    True
    >>> validate_number('12e-3')
    True
    >>> validate_number('12.23e6')
    True

    >>> validate_number('x')
    False
    >>> validate_number('.2')
    False
    >>> validate_number('0.23.3')
    False
    >>> validate_number('2e')
    False
    >>> validate_number('-')
    False

    Doesn't accept unnescessary leading or trailing zero'
    >>> validate_number('01.23')
    False
    >>> validate_number('1.0')
    False
    '''
    return bool(re.fullmatch(r'-?([1-9][0-9]*|0)(\.[0-9]*[1-9])?(e-?[0-9]+)?', s))
