from typing import Self


class Fib:
    def __init__(self) -> None:
        self._curr: int = 0
        self._next: int = 1

    def __repr__(self) -> str:
        return f"{self._curr}"

    def advance(self) -> None:
        next = self._curr + self._next
        self._curr = self._next
        self._next = next


class FibIter(Fib):
    def __init__(self) -> None:
        super().__init__()  # IMPORTANT!

    def __iter__(self) -> Self:
        self._curr: int = 0
        self._next: int = 1
        return self

    def __next__(self) -> int:
        curr = self._curr
        self.advance()
        return curr
