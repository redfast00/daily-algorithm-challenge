import re


def reverse_sentence(sentence):
    '''Reverses the order of words in a sentence while preserving the order of delimiters.

    >>> reverse_sentence('one/two.three,four')
    'four/three.two,one'
    >>> reverse_sentence('/one.two?')
    '/two.one?'
    >>> reverse_sentence('one...two/three')
    'three...two/one'
    >>> reverse_sentence('one{two}three')
    'three{two}one'
    '''

    # Find all words in sentence
    words = re.findall(r'\w+', sentence)
    # Escape curly braces (alternative: use regex, this saves a replace call)
    escaped = sentence.replace('{', '{{').replace('}', '}}')
    # Replace all words by {}
    formatstring = re.sub(r'\w+', '{}', escaped)
    # Put words in reverse order back in formatstring
    return formatstring.format(*reversed(words))
