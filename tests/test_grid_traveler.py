from dynamic_programming.grid_traveler import get_step_count


def test_grid_traveler_result():
    assert get_step_count(1, 1) == 1
    assert get_step_count(2, 3) == 3
    assert get_step_count(3, 2) == 3
    assert get_step_count(3, 3) == 6
    assert get_step_count(100, 100)
