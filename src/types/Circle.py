# https://docs.python.org/3/library/typing.html
import math
from typing import TypeVar, Type

C = TypeVar('C', bound='Circle')

class Circle:
    """An abstract circle"""

    def __init__(self, radius: float) -> None:
        self.radius = radius

    # Use a type variable to show that the return type
    # will always be an instance of whatever ``cls`` is
    @classmethod
    def with_circumference(cls: Type[C], circumference: float) -> C:
        """Create a circle with the specified circumference"""
        radius = circumference / (math.pi * 2)
        return cls(radius)


class Tire(Circle):
    """A specialised circle (made out of rubber)"""

    MATERIAL = 'rubber'

c = Circle.with_circumference(3)  # Ok, variable 'c' has type 'Circle'
t = Tire.with_circumference(4)  # Ok, variable 't' has type 'Tire' (not 'Circle')