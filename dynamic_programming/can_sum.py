"""
Given a list of numbers (numbers) checks whether any combination of these numbers
can sum up to a target number (n)

E.g.
    can_sum(7, [2, 3, 5]) -> True
        options:
            - [2, 2, 3]
            - [3, 5]
"""


def can_sum(n: int, numbers: [int], memo: dict = None) -> bool:
    """
    Returns whether any combination of a given list of numbers can sum up to a target number.

    Brute force complexity:
    Time: O(n^m)
    Space: O(m)

    Memoized complexity:
    Time: O(n * m)
    Space: O(m)

    :param n: Target value
    :param numbers: List of numbers to be summed up
    :param memo: Dictionary to hold common repetitive results
    :return: Boolean
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return True
    if n < 0:
        return False
    for current in numbers:
        remainder = n - current
        result = can_sum(remainder, numbers, memo)
        if result:
            memo[n] = True
            return True
    memo[n] = False
    return False
