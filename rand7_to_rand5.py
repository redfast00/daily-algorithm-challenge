import random


def rand7():
    return random.randint(1, 7)


def rand5():
    generated = rand7()
    while generated > 5:
        generated = rand7()
    return generated
