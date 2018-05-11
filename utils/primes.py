import math


def factorize(number):
    result = []
    while number != 1:
        # Inclusive range
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                result.append(i)
                number = number // i
                break
        else:
            result.append(number)
            # Break out of while loop
            break
    return result
