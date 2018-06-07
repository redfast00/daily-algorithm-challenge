def split_into_chunks(s, k):
    '''Splits a sentence into lines that are no longer than k characters, without breaking lines.

    >>> split_into_chunks("This is a test", 10)
    ['This is a', 'test']
    >>> split_into_chunks("This is technology", 10)
    ['This is', 'technology']
    >>> split_into_chunks("These are cool technologies", 10)

    '''
    result = []
    current = []
    current_length = -1
    for word in s.split():
        new_length = len(word)
        if new_length > k:
            return
        elif current_length + 1 + new_length > k:
            result.append(' '.join(current))
            current = [word]
            current_length = new_length
        else:
            current.append(word)
            current_length += new_length + 1
    result.append(' '.join(current))
    return result
