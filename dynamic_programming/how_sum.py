"""
Given a list of numbers (values) returns a combination of numbers that
can sum up to a target number (n)

E.g.
    how_sum(8, [2, 3, 7]) -> [2, 2, 2, 2]
"""


def how_sum(n: int, values: [int], memo: dict = None) -> [int]:
    """
    Returns the combination of numbers from a given list (values)
    that can sum up to a target number.

    :param n: Target number
    :param values: List of numbers to be checked
    :param memo: Dictionary holding common repetitive results
    :return: List of numbers
    """

    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return []
    if n < 0:
        return None
    for current in values:
        remainder = n - current
        result = how_sum(remainder, values, memo)
        if result is not None:
            result.append(current)
            memo[n] = result
            return memo[n]

    memo[n] = None
    return memo[n]