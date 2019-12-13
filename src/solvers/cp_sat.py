"""
"""

from ortools.sat.python import cp_model

from solvers.base import BaseSolver
from util.solution_printer import SolutionPrinter


class CpSatSolver(BaseSolver):
    """
    """

    def __init__(self, n, print_solutions=False):
        """
        """

        super().__init__(n, print_solutions)

        self._model = cp_model.CpModel()

        queens = [
            self._model.NewIntVar(0, self._n - 1, 'x%i' % i)
            for i in range(self._n)
        ]

        # Constraint: All Queens should be in Different Rows
        self._model.AddAllDifferent(queens)

        # Constraint: No Two Queens should be on the Same Diagonal
        for i in range(self._n):

            diag1 = []
            diag2 = []

            for j in range(self._n):

                q1 = self._model.NewIntVar(0, 2 * self._n, 'diag1_%i' % i)
                diag1.append(q1)
                self._model.Add(q1 == queens[j] + j)

                q2 = self._model.NewIntVar(-self._n, self._n, 'diag2_%i' % i)
                diag2.append(q2)
                self._model.Add(q2 == queens[j] - j)

            self._model.AddAllDifferent(diag1)
            self._model.AddAllDifferent(diag2)

        self._solver = cp_model.CpSolver()
        self._solution_printer = SolutionPrinter(queens, self._print_solutions)

    def _solve(self):
        """
        """

        status = self._solver.SearchForAllSolutions(
            self._model, self._solution_printer)

        return self._solution_printer.solution_count()
