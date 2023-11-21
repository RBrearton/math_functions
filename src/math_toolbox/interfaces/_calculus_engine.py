"""
This module contains the ICalculusEngine interface, which must be implemented by all
calculus engines.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ._function import IFunction


class ICalculusEngine(ABC):
    """
    The ICalculusEngine interface defines everything that a calculus engine needs to be
    able to do.
    """

    @abstractmethod
    def with_respect_to(self, variable: str) -> "IFunction":
        """
        This method applies the current calculus engine to the given variable, returning
        a new function.
        """
