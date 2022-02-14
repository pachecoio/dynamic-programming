def can_sum(n: int, numbers: [int], memo: dict = None) -> bool:
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
