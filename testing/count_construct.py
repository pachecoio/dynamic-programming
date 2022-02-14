import re


def count_construct(target: str, word_bank: [str], memo: dict = None) -> int:
    """
    Given a target word and a list of words, returns a count
    of the possible concatenation of the words from the bank that
    result in the target word.

    Brute force complexity:
    Time: O(n^m)
    Space: O(m^2)

    Memoized complexity:
    Time: O(n * m)
    Space: O(m^2)

    :param target: desired string value
    :param word_bank: list of words
    :param memo: common result values memoized
    :return: int
    """
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if not target:
        return 1

    count = 0
    for word in word_bank:
        expression = f"^{word}"
        match = re.match(expression, target)
        if bool(match):
            remainder = re.sub(expression, '', target)
            result = count_construct(remainder, word_bank, memo)
            count += result

    memo[target] = count
    return count
