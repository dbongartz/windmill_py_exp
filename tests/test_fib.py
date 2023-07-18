from itertools import islice
from fib_py.fib import Fib, FibIter, fib_generator


def test_fib():
    dut = Fib()
    expected: list[int] = [0, 1, 1, 2, 3, 5, 8]
    actual: list[int] = list()

    for _ in range(0, len(expected)):
        actual.append(dut._curr)
        dut.advance()

    assert expected == actual


def test_fib_iter():
    dut = FibIter()
    expected: list[int] = [0, 1, 1, 2, 3, 5, 8]
    actual: list[int] = list(islice(dut, 0, len(expected)))

    assert expected == actual


def test_fib_gen():
    dut = fib_generator()
    expected: list[int] = [0, 1, 1, 2, 3, 5, 8]
    actual: list[int] = list(islice(dut, 0, len(expected)))

    assert expected == actual
