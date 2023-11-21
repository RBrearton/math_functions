"""
This file contains the ContFunction class, which is used to represent a general
continuous function.
"""

from typing import Callable

from .interfaces import IDifferentiationEngine, IFunction, IIntegrationEngine, IMathSet


class RealFunction(IFunction):
    """
    This class represents a general continuous real function. Most functions are
    instances of RealFunction.
    """

    def __init__(self, function_to_call: Callable) -> None:
        self._function = function_to_call

    @property
    def integrate(self) -> IIntegrationEngine:
        raise NotImplementedError()

    @property
    def differentiate(self) -> IDifferentiationEngine:
        raise NotImplementedError()

    @property
    def domain(self) -> "IMathSet":
        raise NotImplementedError()

    @property
    def codomain(self) -> "IMathSet":
        raise NotImplementedError()

    def evaluate(self, arguments: tuple[float, ...]) -> float:
        return self._function(*arguments)

    def plot(self):
        raise NotImplementedError()
