"""
This module contains the IMathSet interface, which is used to represent a general
mathematical set. The name of this interface has been chosen to avoid confusion with
the Python set data structure.
"""

from abc import ABC, abstractmethod


class IMathSet(ABC):
    """
    This interface defines what mathematical sets must implement.
    """

    @abstractmethod
    def __repr__(self) -> str:
        """
        The string representation of this mathematical set. This must uniquely identify
        the mathematical set.
        """
