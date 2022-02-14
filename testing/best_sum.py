def best_sum(n: int, values: [int]) -> [int]:
    """
    Brute force implementation:
    time: O(n^m * m)
    space: O(m^2)
    """
    if n == 0:
        return []
    if n < 0:
        return
    result = None
    for current in values:
        remainder = n - current
        r = best_sum(remainder, values)
        if r is not None:
            r.append(current)
            result = r if result is None or len(r) < len(result) else result
    return result


def best_sum_memoized(n: int, values: [int], memo: dict = None) -> [int]:
    """
    memoized implementation:
    time: O(m^2 * n)
    space: O(m^2)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return []
    if n < 0:
        return
    result = None
    for current in values:
        remainder = n - current
        r = best_sum_memoized(remainder, values, memo)
        if r is not None:
            r.append(current)
            result = r if result is None or len(r) < len(result) else result
    memo[n] = result
    return result
