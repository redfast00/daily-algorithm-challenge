import re


def find_longest_path_length(path):
    r'''Finds the longest path to a file in a representation of a filesystem.
    >>> find_longest_path_length("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") # noqa
    32
    >>> find_longest_path_length("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
    20

    '''
    stack = []
    result = 0
    # regex captures tabs in a group and the name in the second group
    for match in re.finditer(r'(\t*)([\w\.]+)', path):
        indents = len(match[1]) + 1
        name = match[2]
        if '.' in name:
            # File
            # This can be made faster by saving current length of the directories on the stack
            result = max(len('/'.join(stack) + f'/{name}'), result)
        else:
            # Directory
            while len(stack) >= indents:
                stack.pop()
            if len(stack) < indents:
                stack.append(name)
    return result
