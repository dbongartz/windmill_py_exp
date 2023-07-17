"""
Windmill Class

Represents a windmill.

1. Should be able to track its rotations.
2. Can take a windspeed and duration of that windspeed to calculate rotations.
"""

# from dataclasses import dataclass


# @dataclass
class Windmill:
    def __init__(self) -> None:
        self.rotations = 0

    def __repr__(self) -> str:
        return f"Windmill has {self.rotations} rotations."


wm: Windmill = Windmill()

print(wm)
