def reverse_sentence(sentence):
    '''Reverses the order of words in a sentence.

    >>> reverse_sentence('one two three four')
    'four three two one'
    >>> reverse_sentence('only')
    'only'
    >>> reverse_sentence('')
    ''
    '''
    return ' '.join(reversed(sentence.split(' ')))


def reverse_list_inplace(l, start, stop):
    for idx in range(start, start + (stop - start) // 2):
        other_idx = stop - 1 - (idx - start)
        l[idx], l[other_idx] = l[other_idx], l[idx]
    return l


def reverse_sentence_inplace(character_list):
    '''Reverses the order of words in the character list.

    >>> ''.join(reverse_sentence_inplace(list('one two three four')))
    'four three two one'
    >>> ''.join(reverse_sentence_inplace(list('only')))
    'only'
    >>> ''.join(reverse_sentence_inplace(list('')))
    ''
    '''
    # First reverse entire list
    reverse_list_inplace(character_list, 0, len(character_list))
    # Reverse individual words in list
    start = 0
    for current_idx, character in enumerate(character_list):
        if character == ' ':
            reverse_list_inplace(character_list, start, current_idx)
            start = current_idx + 1
    # Reverse last word
    reverse_list_inplace(character_list, start, len(character_list))
    return character_list
