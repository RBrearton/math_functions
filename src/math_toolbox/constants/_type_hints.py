"""
This module contains type hints that are used throughout the project.
"""

import numpy as np


class TypeHints:
    """
    This class contains type hints that are used throughout the project.
    """

    numeric = int | float | complex | np.number
    """
    This type hint represents any individual numeric value. This number could be an
    element of an arbitrary field.
    """

    real = int | float | np.number
    """
    This type hint represents any real number.
    """
