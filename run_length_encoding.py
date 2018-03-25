import re


def decode(s):
    '''Decodes a run-length encoded string.

    >>> decode('4A3B2C1D2A')
    'AAAABBBCCDAA'
    >>> decode('4A11B2C')
    'AAAABBBBBBBBBBBCC'
    '''
    result = []
    for match in re.finditer(r'(?P<amount>\d+)(?P<character>\D)', s):
        result.append(match.group('character') * int(match.group('amount')))
    return ''.join(result)


def encode(s):
    '''Encodes a string using run-length encoding.

    >>> encode('AAAABBBCCDAA')
    '4A3B2C1D2A'
    >>> encode('AAAABBBBBBBBBBBCC')
    '4A11B2C'
    '''
    result = []
    for match in re.finditer(r'((.)\2*)', s):
        character = match.group(1)
        result.append(f'{len(character)}{character[0]}')
    return ''.join(result)
