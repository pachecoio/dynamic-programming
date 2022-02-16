"""
Find the fibonacci sequence of a given number
"""


def fib(number: int) -> int:
    if number <= 2:
        return 1
    return fib(number - 1) + fib(number - 2)


def fib_memoized(number: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    if number in memo:
        return memo[number]
    if number <= 2:
        return 1
    memo[number] = fib_memoized(number - 1, memo) + fib_memoized(number - 2, memo)
    return memo[number]


def fib_tabulation(number: int) -> int:
    n = number + 1
    _list = [0] * n
    _list[1] = 1
    for index, current in enumerate(_list):
        if index > 0:
            if index + 1 < n:
                _list[index + 1] += _list[index]
            if index + 2 < n:
                _list[index + 2] += _list[index]
    return _list[number]
