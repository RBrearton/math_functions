"""
This module contains the IIntegrationEngine interface, which must be implemented by all
integration engines.
"""

from ._calculus_engine import ICalculusEngine


class IIntegrationEngine(ICalculusEngine):
    ...
