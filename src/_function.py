"""
This file contains the ContFunction class, which is used to represent a general
continuous function.
"""

from abc import ABC, abstractmethod


class Function(ABC):
    """
    This class represents a general continuous function.
    """

    @abstractmethod
    def __call__(self, x):
        """
        This method returns the value of the function at the given point.
        """
