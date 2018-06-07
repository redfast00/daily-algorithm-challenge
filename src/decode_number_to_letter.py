def logger(function):
    '''Wrapper to inspect recursive functions.'''
    def inner(*args, **kwargs):
        result = function(*args, **kwargs)
        print(f'"{args[0]}" -> {result}')
        return result
    return inner


def num_combinations(code):
    '''Returns the number of possible ways to decode a numberstring, where a = 1,
    b = 2, ..., z = 26.
    111 -> aaa, ak, ka
    >>> num_combinations('111')
    3
    >>> num_combinations('121')
    3
    >>> num_combinations('128')
    2
    >>> num_combinations('1111')
    5
    >>> num_combinations('11111')
    8
    >>> num_combinations('10')
    1
    >>> num_combinations('101')
    1
    >>> num_combinations('204')
    1
    >>> num_combinations('110')
    1
    >>> num_combinations('04')
    0
    '''
    if len(code) == 1:
        return 0 if code == '0' else 1
    elif len(code) == 2:
        # max two combinations: each digit is a letter or the two digits form one letter
        return 0 if code[0] == '0' else ('0' not in code) + (1 <= int(code) <= 26)
    else:
        # check if last number is '0'
        if num_combinations(code[-1]):
            total = num_combinations(code[:-1])
            if num_combinations(code[-2:]) == 2:
                total += num_combinations(code[:-2])
            return total
        else:
            return num_combinations(code[-2:]) * num_combinations(code[:-2])
        return total
