from testing.how_sum import how_sum


def test_how_sum():
    assert how_sum(8, [2, 3, 5]) == [2, 2, 2, 2]
    assert how_sum(4, [4]) == [4]
    assert not how_sum(300, [7, 14])
