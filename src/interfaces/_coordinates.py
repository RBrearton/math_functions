"""
This file contains the ICoordinates interface, which is used to represent a general
set of coordinates. Functions take coordinates as inputs.
"""

from abc import ABC, abstractmethod

import numpy as np


class ICoordinates(ABC):
    """
    This interface represents a general set of coordinates.
    """

    @classmethod
    @abstractmethod
    def from_array(cls, array: np.ndarray) -> "ICoordinates":
        """
        This method returns a set of coordinates from the given array.
        """
