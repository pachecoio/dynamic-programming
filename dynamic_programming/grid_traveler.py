"""
Given a grid find the amount of steps to go from the start cell to the last cell.

E.g.
    [
        [start, 0 ,  0 ],
        [  0  , 0 , end],
    ]
    get_step_count(2, 3) -> 3
"""


def get_step_count(rows: int, columns: int, memo: dict = None) -> int:
    """
    Returns the total count of the steps necessary to go from the start cell to the end cell
    of a grid

    Brute force complexity:
    Time: O(2^(n+m))
    Space: O(n + m)

    Memoized complexity:
    Time: O(n * m)
    Space(n + m)


    :param rows: int -> amount of rows
    :param columns: int -> amount of columns
    :param memo: dict -> dictionary holding common repetitive results
    :return: int -> Total count
    """
    if memo is None:
        memo = {}
    key = f'{rows},{columns}'
    reversed_key = f'{columns},{rows}'
    if key in memo:
        return memo[key]
    if rows == 1 and columns == 1:
        return 1
    if rows == 0 or columns == 0:
        return 0
    memo[key] = get_step_count(rows - 1, columns, memo) + get_step_count(rows, columns - 1, memo)
    memo[reversed_key] = memo[key]
    return memo[key]