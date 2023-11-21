"""
This file contains the VectorSpace interface, which is used to represent a general
vector space.
"""

from abc import ABC, abstractmethod


class IVectorSpace(ABC):
    """
    This interface defines what vector spaces must implement.
    """

    @abstractmethod
    def __repr__(self) -> str:
        """
        The string representation of this vector space. This must uniquely identify the
        vector space.
        """
