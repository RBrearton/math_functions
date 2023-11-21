"""
This module contains the IMathSet interface, which is used to represent a general
mathematical set. The name of this interface has been chosen to avoid confusion with
the Python set data structure.
"""

from abc import ABC, abstractmethod

from ..constants import TypeHints


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

    @abstractmethod
    def __contains__(self, element: TypeHints.numeric) -> bool:
        """
        This method returns True if the element is in the set, and False otherwise.

        Args:
            element: The element.

        Returns:
            Whether or not the element is in the set.
        """

    @abstractmethod
    def is_subset(self, other: "IMathSet") -> bool:
        """
        This method returns True if this set is a subset of the other set, and False
        otherwise.

        Args:
            other: The other set.

        Returns:
            True if this set is a subset of the other set, and False otherwise.
        """

    @abstractmethod
    def is_superset(self, other: "IMathSet") -> bool:
        """
        This method returns True if this set is a superset of the other set, and False
        otherwise.

        Args:
            other: The other set.

        Returns:
            True if this set is a superset of the other set, and False otherwise.
        """
