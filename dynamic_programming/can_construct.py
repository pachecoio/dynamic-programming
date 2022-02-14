import re

"""
Given a list of words (word_bank) check if any combination of words concatenated
can form the target word (target)

E.g.
    can_construct('skate', ['s', 'kat', 'e']) -> True
"""


def can_construct(target: str, word_bank: [str], memo: dict = None) -> bool:
    """
    Returns whether a combination of words in a list can form a target word

    Brute force complexity:
    Time: O(n^m)
    Space: O(m^2)

    Memoized complexity:
    Time: O(n * m)
    Space: O(m^2)

    :param target: Target word
    :param word_bank: list of words to be concatenated
    :param memo: dictionary to hold common repetitive states
    :return: Boolean
    """
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
