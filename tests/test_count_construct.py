from testing.count_construct import count_construct


def test_count_construct():
    assert count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']) == 1
    assert count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) == 2
    assert count_construct('skateboard', [
        'bo',
        'rd',
        'ate',
        't',
        'ska',
        'sk',
        'boar'
    ]) == 0
    assert count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee'
    ]) == 0
