import random
from collections import Counter


def rand5():
    '''Returns a random number from 1 to 5 (inclusive).'''
    return random.randrange(1, 6)


def rand7():
    '''Returns a random number from 1 to 7 (inclusive).'''
    while True:
        first = rand5() - 1
        second = rand5() - 1
        result = 5 * first + second
        if result < 21:
            return (result % 7) + 1


if __name__ == '__main__':
    print(Counter(rand7() for _ in range(7000000)))
