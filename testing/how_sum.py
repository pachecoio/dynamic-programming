def how_sum(n: int, values: [int], memo: dict = None) -> [int]:
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