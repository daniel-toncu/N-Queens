"""
"""

import time


class BaseSolver:
    """
    """

    def __init__(self, n, print_solutions=False):
        """
        """

        self._n = n
        self._print_solutions = print_solutions

        self._solutions = 0

    def solve(self):
        """
        """

        start = time.clock()
        result = self._solve()
        end = time.clock()

        return (end - start, result)

    def _solve(self):
        """
        """

        raise Exception("Not Implemented.")
