# Generate the next number in a fibonacci series and print it

from copy import copy
from typing import Tuple

from fib import Fib
from fib import FibIter

# ================================================= #
print("Naive:")
curr = 0
print(curr)

curr = 1
print(curr)

curr = 1
print(curr)

curr = 2
print(curr)

curr = 3
print(curr)
# and so on...

# Naive Iterative
print("Iterative:")
curr = 0
next = 1
print(curr)

for _ in range(0, 5):
    next_next = curr + next
    curr = next
    next = next_next
    print(curr)


# ================================================= #
print("Function tuple:")


def fib_next_tuple(curr: int, next: int) -> Tuple[int, int]:
    return next, curr + next


curr, next = (0, 1)
print(curr)

for _ in range(0, 5):
    curr, next = fib_next_tuple(curr, next)
    print(curr)


# ================================================= #
print("Class without methods (aka struct) + functional style (immutable)")


class FibImmutable:
    def __init__(self) -> None:
        self.curr = 0
        self.next = 1


def fib_advance_functional(fib: FibImmutable) -> FibImmutable:
    new_fib = copy(fib)

    next = new_fib.curr + new_fib.next
    new_fib.curr = new_fib.next
    new_fib.next = next

    return new_fib


fib = FibImmutable()
print(fib.curr)

for _ in range(0, 5):
    fib = fib_advance_functional(fib)
    print(fib.curr)


# ================================================= #
print("Class without methods (aka struct) + function (mutable)")


class FibMutable:
    def __init__(self) -> None:
        self.curr: int = 0
        self.next: int = 1


def fib_advance_mutable(fib: FibMutable) -> None:
    next = fib.curr + fib.next
    fib.curr = fib.next
    fib.next = next


fib = FibMutable()
print(fib.curr)

for _ in range(0, 5):
    fib_advance_mutable(fib)
    print(fib.curr)

# ================================================= #
print("Class with methods")


fib = Fib()
print(fib)

for _ in range(0, 5):
    fib.advance()
    print(fib)


# ================================================= #
print("Class extend with iterator")

fib = FibIter()
for i, f in enumerate(fib):
    if i > 4:
        break
    print(f)

# ================================================= #
print("Class with methods advanced iter directly")

for i, f in enumerate(FibIter()):
    if i > 4:
        break
    print(f)
