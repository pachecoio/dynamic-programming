from dynamic_programming.fibonacci_sequence import fib, fib_memoized, fib_tabulation


def test_get_fibonacci_sequence():
    assert fib(6) == 8


def test_get_fibonacci_sequence_memoized():
    assert fib_memoized(40) == 102334155


def test_get_fibonacci_tabulated():
    assert fib_tabulation(6) == 8
    assert fib_memoized(40) == 102334155
