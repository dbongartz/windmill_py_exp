from typing import Self, Generator


# Class with __repr__ and example for Iterator (commented out)
class Fib:
    def __init__(self) -> None:
        self._curr: int = 0
        self._next: int = 1

    def __repr__(self) -> str:
        return f"{self._curr}"

    def advance(self) -> None:
        self._curr, self._next = (self._next, self._curr + self._next)

    # Equivalent to FibIter without class extension (inheritance)
    # def __iter__(self) -> Self:
    #     self._curr: int = 0
    #     self._next: int = 1
    #     return self

    # def __next__(self) -> int:
    #     curr = self._curr
    #     self.advance()
    #     return curr


# Class extension / inheritance
class FibIter(Fib):
    def __init__(self) -> None:
        super().__init__()  # IMPORTANT! inheritance

    def __iter__(self) -> Self:
        self._curr: int = 0
        self._next: int = 1
        return self

    def __next__(self) -> int:
        curr = self._curr
        self.advance()
        return curr


# Generator function doing the same as Iterator
def fib_generator(n: int | None = None) -> Generator[int, None, None]:
    curr, next = (0, 1)
    if n:
        for _ in range(n):
            yield curr
            curr, next = (next, curr + next)
    else:
        while True:
            yield curr
            curr, next = (next, curr + next)
