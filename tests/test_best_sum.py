from dynamic_programming.best_sum import best_sum, best_sum_memoized


def test_best_sum():
    assert best_sum(7, [5, 3, 4, 7]) == [7]
    assert best_sum(8, [2, 3, 5]) == [5, 3]
    # assert best_sum(400, [1, 2, 3, 4]) # would take forever


def test_best_sum_memoized():
    assert best_sum_memoized(7, [5, 3, 4, 7]) == [7]
    assert best_sum_memoized(8, [2, 3, 5]) == [5, 3]
    assert best_sum_memoized(100, [1, 3])
