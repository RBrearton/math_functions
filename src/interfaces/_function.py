"""
This module contains the IFunction interface, which must be implemented by all
functions.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from ._differentiation_engine import IDifferentiationEngine
    from ._integration_engine import IIntegrationEngine
    from ._math_set import IMathSet


class IFunction(ABC):
    """
    The IFunction interface defines everything that a function needs to be able to do.
    In the mathematical world, a function is something that maps a number to a number.
    Of course, we can get rather specific about the kind of number that we input and
    the kind of number that we output, and we can talk about functions of multiple
    variables requiring multiple inputs, but the spirit of the definition remains the
    same - a few numbers in, one number out.

    It would be possible for us to define a computational analogue to this relatively
    straightforwardly by requiring that, to describe a mathematical function, we just
    need to define one python function that takes one number (or a tuple of numbers for
    functions of multiple arguments) as an argument, and returns one number as an
    output.

    The critical issue is that, if we wanted to do something very reasonable, like plot
    or integrate the function, we would need to evaluate the function at many points.
    That would mean executing the function thousands of times. It would be far more
    efficient to change our definition of a function from being something that maps a
    single set of inputs to a single output, to being something that can map a very
    large number of sets of inputs to a very large number of outputs.

    This is the reason why, to implement the IFunction interface, you must define a
    method called evaluate, which takes at least one numpy array as an argument, and
    returns one numpy array as an output. The kth element of the output array
    corresponds to the value of the function at the kth point in the input array (or
    input arrays if the function takes more than one argument).
    """

    @property
    @abstractmethod
    def integrate(self) -> "IIntegrationEngine":
        """
        This method returns an integration engine that can be used to integrate the
        function.
        """

    @property
    @abstractmethod
    def differentiate(self) -> "IDifferentiationEngine":
        """
        This method returns a differentiation engine that can be used to differentiate
        the function.
        """

    @property
    @abstractmethod
    def domain(self) -> "IMathSet":
        """
        This method returns the domain of the function. Note that it's in general
        tricky to work out the domain of a function, so implementations of this method
        may return a superset of the true domain.
        """

    @property
    @abstractmethod
    def codomain(self) -> "IMathSet":
        """
        This method returns the codomain of the function.
        """

    @abstractmethod
    def evaluate(self, arguments: np.ndarray | tuple[np.ndarray, ...]) -> np.ndarray:
        """
        This method returns the value of the function at the given point.
        """

    @abstractmethod
    def plot(self):
        """
        This method provides a simple interface to generate a hassle-free plot of the
        function.
        """


def _test(function: IFunction):
    # Returns a function that takes one fewer arguments than the original function.
    function.integrate.with_respect_to("x")

    # Returns another function with the same number of arguments as the original
    # function.
    function.differentiate.with_respect_to("x")
