import re
"""
Given a list of words (word_bank) check if any combination of words concatenated
can form the target word (target) and return the list of the possible combinations

E.g.
    all_construct('skate', ['s', 'kat', 'e', 'test']) -> [['s', 'kat', 'e']]
"""


def all_construct(target: str, word_bank: [str], memo: dict = None) -> [[str]]:
    """
    Complexity:
    Time: O(n^m)
    Space: O(m)

    :param target: Target word
    :param word_bank: list of words to be checked and combined
    :param memo:
    :return: list of possible combinations
    """
    if not memo:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    construct_ways = []

    for word in word_bank:
        expression = f'^{word}'
        is_match = re.match(expression, target)
        if is_match:
            remainder = re.sub(expression, '', target)
            suffix_ways = all_construct(remainder, word_bank, memo)
            target_ways = [
                [word, *w] for w in suffix_ways
            ]
            construct_ways.extend(target_ways)

    memo[target] = construct_ways
    return construct_ways
