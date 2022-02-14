def get_step_count(rows: int, columns: int, memo: dict = None) -> int:
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