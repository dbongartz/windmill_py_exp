# Fibonacci: 0 1 1 2 3 5 8 13

from typing import List

# loop 1

fib_current = 0
fib_next = 1
for _ in range(5):
    # procedural syntax
    tmp = fib_next
    fib_next = fib_next + fib_current
    print(fib_current)
    fib_current = tmp


# loop 2
fib_current = 0
fib_next = 1
fib_list = []
for _ in range(7):
    fib_list.append(fib_current)
    # tuple syntax
    fib_current, fib_next = (fib_next, fib_next + fib_current)

expected = [0, 1, 1, 2, 3, 5, 8]

assert expected == fib_list
print(fib_list)


# Iterative function
def fibonaccis(length: int) -> List[int]:
    fib_current = 0
    fib_next = 1
    fib_list = []
    for _ in range(length):
        fib_list.append(fib_current)
        fib_current, fib_next = (fib_next, fib_next + fib_current)
    return fib_list


assert expected == fibonaccis(7)


# Generate (NOT using python generators)
def fib_generate(fib_current, fib_next):
    fib_current, fib_next = (fib_next, fib_next + fib_current)
    return fib_current, fib_next


fib_curr, fib_next = (0, 1)  # 0, 1
fib_curr, fib_next = fib_generate(fib_curr, fib_next)  # 1, 1
fib_curr, fib_next = fib_generate(fib_curr, fib_next)  # 1, 2
fib_curr, fib_next = fib_generate(fib_curr, fib_next)  # 2, 3

assert fib_curr == 2 and fib_next == 3


# Class

class Fib:
    def __init__(self):
        self.curr: int = 0
        self.next: int = 1

    # Associated method, "self" has special meaning being of type of class: Fibb
    def generate_next(self) -> int:
        tmp = self.curr # Needed to return 0 first
        self.curr, self.next = (self.next, self.next + self.curr)
        return tmp


# Free method, "self" has no special meaningg
# It is just parameter name, could be "fibs"
def generate_next_free(self: Fib) -> int:
    tmp = self.curr
    # We are MODIFYING self here
    # Passing objects in python always means I can read and write
    # to the original object, not a copy
    self.curr, self.next = (self.next, self.next + self.curr)
    return tmp


# Object (= instance of class)
fibs: Fib = Fib()
fib_curr = generate_next_free(fibs)  # 0 # Free method
fib_curr = Fib.generate_next(fibs)  # 1 # Associated method, explicit syntax (less common)
fib_curr = fibs.generate_next()  # 1 # Associated method, implicit syntax (common)
fib_curr = generate_next_free(fibs)  # 2
fib_curr = generate_next_free(fibs)  # 3

assert 3 == fib_curr
