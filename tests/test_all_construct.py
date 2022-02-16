from dynamic_programming.all_construct import all_construct


def test_all_construct():
    result = all_construct('skateboard', ['s', 'kat', 'e' 'boar', 'd', 'skate', 'board', 'testing'])

    assert result == [
        ['s', 'kat', 'e' 'boar', 'd'],
        ['skate', 'board'],
    ]
