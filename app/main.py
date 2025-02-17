from __future__ import annotations
# For supporting annotations in older version

from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float]) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        raise TypeError("Unsupported type for addition")

    def __iadd__(self, other: Union[Distance, float]) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError("Unsupported type for in-place addition")
        return self

    def __mul__(self, other: float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Union[Distance, float]) -> bool:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: Union[Distance, float]) -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: Union[Distance, float]) -> bool:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __ne__(self, other: Union[Distance, float]) -> bool:
        return self.km != (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: Union[Distance, float]) -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: Union[Distance, float]) -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)
