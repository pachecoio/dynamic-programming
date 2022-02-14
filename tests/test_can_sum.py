from dynamic_programming.can_sum import can_sum


def test_can_sum():
    assert can_sum(7, [7])
    assert not can_sum(7, [5])
    assert can_sum(7, [4, 3])
    assert not can_sum(300, [7, 14, 49])
