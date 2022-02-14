import re


def can_construct(target: str, word_bank: [str], memo: dict = None) -> bool:
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    if not target:
        return True

    for word in word_bank:
        expression = f"^{word}"
        match = re.match(expression, target)
        if bool(match):
            remainder = re.sub(expression, '', target)
            result = can_construct(remainder, word_bank, memo)
            if result:
                memo[target] = result
                return True
    memo[target] = False
    return False
