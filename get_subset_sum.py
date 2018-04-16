def subset_sum(k, lst):
    '''Returns a subset of lst that has a sum of k.

    >>> sum(subset_sum(24, [12, 1, 61, 5, 9, 2]))
    24
    >>> subset_sum(53, [12, 13, 14])
    '''
    return recursive_calculate(k, sorted(lst, reverse=True), 0)


def recursive_calculate(k, lst, start):
    for idx in range(start, len(lst)):
        if lst[idx] > k:
            continue
        elif lst[idx] == k:
            return [lst[idx]]
        else:
            rest = recursive_calculate(k - lst[idx], lst, idx + 1)
            if rest is not None:
                rest.append(lst[idx])
                return rest
