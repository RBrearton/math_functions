"""
This module contains the base class for all intervals.
"""

from ...interfaces import IInterval


class IntervalBase(IInterval):
    """
    This is the base class for all intervals.
    """

    def __init__(self, lower_bound: float, upper_bound: float) -> None:
        self._lower_bound = lower_bound
        self._upper_bound = upper_bound

    @property
    def lower_bound(self) -> float:
        return self._lower_bound

    @property
    def upper_bound(self) -> float:
        return self._upper_bound
