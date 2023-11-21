"""
This file contains the ContFunction class, which is used to represent a general
continuous function.
"""


from .interfaces import IDifferentiationEngine, IFunction, IIntegrationEngine, IMathSet


class RealFunction(IFunction):
    """
    This class represents a general continuous real function. Most functions are
    instances of RealFunction.
    """

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

    def plot(self):
        raise NotImplementedError()
