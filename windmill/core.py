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

    def get_wear(self):
        pass

    def receive_wind(self, windspeed_ms: int, duration_s: int):
        """
        Applies a windspeed for a duration to the windmill

        rotations = coeff * windspeed * duration
        with coeff = 1
        """
        coeff = 1
        # self.rotations = coeff * windspeed_ms * duration_s
        self.rotations = 3500


wm: Windmill = Windmill()

print(wm)
