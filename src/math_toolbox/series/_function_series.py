"""
This script contains the FunctionSeries class, which is used to represent a general
series of functions whose domains and codomains are the real numbers.
"""

from collections.abc import Callable

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
        return self._function(index)

    def compute_sum(self, number_of_terms: int) -> IFunction:
        return sum(self._function(i) for i in range(number_of_terms))

    def compute_infinite_sum(self) -> IFunction:
        raise NotImplementedError()
