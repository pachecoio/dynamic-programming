from dynamic_programming.can_construct import can_construct


def test_can_construct():
    assert can_construct('skate', ['skate'])
    assert can_construct('skate', ['s', 'kat', 'e'])
    assert not can_construct('skateboard', ['bo', 'rd', 'ate', 't'])
    assert not can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
        'e',
        'ee',
        'eee',
        'eeee',
        'eeeee',
        'eeeeee',
    ])
