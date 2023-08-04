from dataclasses import dataclass
from typing import List


@dataclass
class Stuff:
    a: int
    b: int
    c: int
    d: List[int]


def do_something(stuff: Stuff) -> bool:
    return stuff.b == 5


def do_something_simpler(b: int) -> bool:
    return b == 5


def do_smothing_wrapper(stuff: Stuff) -> bool:
    return do_something_simpler(stuff.b)


# real_thing = Stuff(1, 2, 3, [42, 43])

# do_something_simpler(real_thing.b)


## testing


def test_do_smth():
    dut = Stuff(1, 2, 3, [42, 43])
    assert not do_something(dut)


def test_do_smth_simpl():
    dut: int = 5
    assert do_something_simpler(dut)


# def do_something_simpler_mocked(b: int) -> bool:
#     return True

def test_do_smth_wrapper():
    dut = Stuff(1, 2, 3, [42, 43])
    mock.assert_called_with_return(do_something_simpler, True)
    assert do_smothing_wrapper(dut)
