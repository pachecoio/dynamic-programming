import re

"""
Given a target word and a list of words, returns a count
of the possible concatenation of the words from the bank that
result in the target word.

E.g.
    count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) -> 1
"""


def count_construct(target: str, word_bank: [str], memo: dict = None) -> int:
    """
    Finds the combinations of words in a given list that can sum up to
    a target word and returns the total count of combinations.

    Brute force complexity:
    Time: O(n^m)
    Space: O(m^2)

    Memoized complexity:
    Time: O(n * m)
    Space: O(m^2)

    :param target: Target string value
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
