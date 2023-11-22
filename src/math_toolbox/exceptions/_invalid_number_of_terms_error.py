"""
This script contains the InvalidNumberOfTermsError class. This error is raised when an
invalid number of terms is passed to a series' partial sum method.
"""


class InvalidNumberOfTermsError(Exception):
    """
    This class represents an error that is raised when an invalid number of terms is
    passed to a series' partial sum method.
    """

    def __init__(self, number_of_terms):
        super().__init__(
            f"The number of terms to sum ({number_of_terms}) is not valid."
        )
        self._number_of_terms = number_of_terms

    @property
    def number_of_terms(self):
        """
        This method returns the invalid number of terms that was passed to the series'
        partial sum method.
        """
        return self._number_of_terms
