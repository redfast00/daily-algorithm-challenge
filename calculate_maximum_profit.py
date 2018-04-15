def calculate_max_profit(prices):
    '''Calculates the maximum profit given a list of prices of a stock
       by buying and selling exactly once.

       >>> calculate_max_profit([9, 11, 8, 5, 7, 10])
       5
       >>> calculate_max_profit([10, 9, 8, 5, 2])
       0
    '''
    smallest_element_so_far = float('inf')
    largest_gain = 0
    for value in prices:
        smallest_element_so_far = min(value, smallest_element_so_far)
        largest_gain = max(value - smallest_element_so_far, largest_gain)
    return largest_gain
