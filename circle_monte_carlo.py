import random


def monte_carlo_pi_search(trials=10000000):
    amount_in_circle = 0
    for _ in range(trials):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            amount_in_circle += 1
    return 4 * amount_in_circle / trials


print(monte_carlo_pi_search())
