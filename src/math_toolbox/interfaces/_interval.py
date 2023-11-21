"""
This file contains the IInterval interface, which must be implemented by all interval
sets.
"""

from abc import abstractmethod

from ._math_set import IMathSet


class IInterval(IMathSet):
    """
    The IInterval interface defines everything that an interval needs to be able to do.
    An interval is a set of real numbers that contains all real numbers between two
    endpoints. The endpoints may or may not be included in the interval.
    """

    @property
    @abstractmethod
    def lower_bound(self) -> float:
        """
        This method returns the lower bound of the interval.
        """

    @property
    @abstractmethod
    def upper_bound(self) -> float:
        """
        This method returns the upper bound of the interval.
        """
