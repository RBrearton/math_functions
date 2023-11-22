"""
This file contains the ISeries interface, which is used to represent a general
mathematical series.
"""

from abc import ABC, abstractmethod

from ._function import IFunction
from ..constants import TypeHints


class ISeries(ABC):
    """
    This interface represents a general mathematical series. This general ISeries
    interface allows for terms in the series to be either numbers or functions.
    """

    @property
    @abstractmethod
    def does_converge(self) -> bool:
        """
        This method returns True if the series converges and False otherwise.
        """

    @abstractmethod
    def compute_term(self, index: int) -> TypeHints.numeric | IFunction:
        """
        This method returns the value of the term at the given index. If index = n,
        then this method returns the value of the nth term in the series.

        Args:
            index:
                The index of the term to compute.

        Returns:
            The value of the term at the given index.

        Raises:
            InvalidTermError:
                This error is raised if an invalid term is requested.
        """

    @abstractmethod
    def compute_partial_sum(
        self, number_of_terms: int
    ) -> TypeHints.numeric | IFunction:
        """
        This method returns the value of the sum of the first n terms in the series.
        Note that, following mathematical convention, the first term in the series will
        set n = 1.

        Args:
            number_of_terms:
                The number of terms to sum.

        Returns:
            The value of the sum of the first n terms in the series.

        Raises:
            InvalidNumberOfTermsError:
                This error is raised if an invalid number of terms is passed to the
                method.

            InvalidTermError:
                This error is raised if a valid number of terms is passed to the method,
                but a term at an invalid index is requested.
        """

    @abstractmethod
    def compute_infinite_sum(self) -> TypeHints.numeric | IFunction:
        """
        This method returns the value of the infinite sum of the series.

        Returns:
            The value of the infinite sum of the series.
        """
