"""
This module contains the ClosedInterval class. This class represents closed intervals of
real numbers.
"""

from ._interval_base import IntervalBase
from ...constants import TypeHints
from ...interfaces import IInterval, IMathSet


class ClosedInterval(IntervalBase):
    """
    This class represents closed intervals of real numbers. A closed interval is a set of
    real numbers that contains all real numbers between two endpoints. The endpoints are
    included in the interval.
    """

    def __init__(self, lower_bound: TypeHints.real, upper_bound: TypeHints.real):
        """
        This method initializes a ClosedInterval object.

        Args:
            lower_bound: The lower bound of the interval.
            upper_bound: The upper bound of the interval.
        """

        super().__init__(lower_bound, upper_bound)

    def __repr__(self) -> str:
        return f"[{self.lower_bound}, {self.upper_bound}]"

    def __contains__(self, element: TypeHints.numeric) -> bool:
        # If the element is complex, then it cannot be in the interval.
        if isinstance(element, complex):
            return False

        return self.lower_bound <= element <= self.upper_bound

    def is_subset(self, other: IMathSet) -> bool:
        if not isinstance(other, IInterval):
            raise NotImplementedError(
                "This method has not been implemented for the given set."
            )

        return (
            self.lower_bound >= other.lower_bound
            and self.upper_bound <= other.upper_bound
        )

    def is_superset(self, other: IMathSet) -> bool:
        if not isinstance(other, IInterval):
            raise NotImplementedError(
                "This method has not been implemented for the given set."
            )

        return (
            self.lower_bound <= other.lower_bound
            and self.upper_bound >= other.upper_bound
        )
