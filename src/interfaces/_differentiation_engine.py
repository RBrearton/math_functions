"""
This module contains the IDifferentiationEngine interface, which must be implemented by
all differentiation engines.
"""

from ._calculus_engine import ICalculusEngine


class IDifferentiationEngine(ICalculusEngine):
    ...
