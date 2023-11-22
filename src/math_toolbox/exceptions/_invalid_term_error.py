"""
This script contains the definition of the InvalidTermError class. This error is
raised when an invalid term is passed to a series.
"""


class InvalidTermError(Exception):
    """
    This class represents an error that is raised when an invalid term is passed to a
    series.
    """

    def __init__(self, term):
        super().__init__(f"The term {term} is not valid term in a series.")
        self._term = term

    @property
    def term(self):
        """
        This method returns the invalid term that was passed to the series.
        """
        return self._term
