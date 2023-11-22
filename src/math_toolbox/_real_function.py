"""
This file contains the ContFunction class, which is used to represent a general
continuous function.
"""

from collections.abc import Callable

import numpy as np
import plotly.graph_objects as go

from .interfaces import (
    IDifferentiationEngine,
    IFunction,
    IIntegrationEngine,
    IInterval,
    IMathSet,
)


class RealFunction(IFunction):
    """
    This class represents a general continuous real function. Most functions are
    instances of RealFunction.
    """

    def __init__(
        self,
        function_to_call: Callable[[np.ndarray | tuple[np.ndarray, ...]], np.ndarray],
    ) -> None:
        self._function = function_to_call

    def __add__(self, other) -> IFunction:
        # Raise an error if the other object isn't a function.
        if not isinstance(other, IFunction):
            raise NotImplementedError(
                "This method has not been implemented for the given object."
            )

        # Define the function to return.
        def function_to_return(arguments: tuple[float, ...]) -> float:
            return self.evaluate(arguments) + other.evaluate(arguments)

        # Return the function.
        return RealFunction(function_to_return)

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

    def evaluate(self, arguments: np.ndarray | tuple[np.ndarray, ...]) -> np.ndarray:
        return self._function(arguments)

    def plot(self, plot_domain: IMathSet, number_of_points: int = 1000):
        # Check that the plot domain is an interval
        if not isinstance(plot_domain, IInterval):
            raise NotImplementedError(
                "Plotting is only implemented over intervals at the moment."
            )

        # Generate the points to plot.
        points = np.linspace(
            plot_domain.lower_bound, plot_domain.upper_bound, number_of_points
        )

        # Evaluate the function at each point.
        values = self.evaluate(points)

        # Plot the function using plotly.
        fig = go.Figure(data=go.Scatter(x=points, y=values))
        fig.show()
