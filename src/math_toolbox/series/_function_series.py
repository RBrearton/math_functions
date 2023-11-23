"""
This script contains the FunctionSeries class, which is used to represent a general
series of functions whose domains and codomains are the real numbers.
"""

from collections.abc import Callable

from ..exceptions import InvalidNumberOfTermsError, InvalidTermError
from ..interfaces import IFunction, ISeries


class FunctionSeries(ISeries):
    """
    This class represents a general series of functions.
    """

    def __init__(self, nth_term_computer: Callable[[int], IFunction]):
        self._function = nth_term_computer

    @property
    def does_converge(self) -> bool:
        raise NotImplementedError()

    def compute_term(self, index: int) -> IFunction:
        # Make sure that the index is positive.
        if index <= 0:
            raise InvalidTermError(index)

        # The index is valid, so return the requested term.
        return self._function(index)

    def compute_partial_sum(self, number_of_terms: int) -> IFunction:
        # Make sure that we were given a positive integer number of terms to sum.
        if number_of_terms <= 0:
            raise InvalidNumberOfTermsError(number_of_terms)

        # Find the requested terms.
        requested_terms = range(1, number_of_terms + 1)

        # Compute the partial sum.
        partial_sum = self.compute_term(1)
        for term in requested_terms[1:]:
            partial_sum += self.compute_term(term)

        # Return the computed partial sum.
        return partial_sum

    def compute_infinite_sum(self) -> IFunction:
        raise NotImplementedError()
