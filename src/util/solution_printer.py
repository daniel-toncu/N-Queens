"""
"""

from ortools.sat.python import cp_model


class SolutionPrinter(cp_model.CpSolverSolutionCallback):
    """
    """

    def __init__(self, variables, print_solutions=False):
        """
        """

        cp_model.CpSolverSolutionCallback.__init__(self)

        self.__variables = variables
        self.__print_solutions = print_solutions

        self.__solution_count = 0

    def OnSolutionCallback(self):
        """
        """

        self.__solution_count += 1

        if not self.__print_solutions:
            return

        n = len(self.__variables)

        board = [
            [0 for _ in range(n)]
            for _ in range(n)
        ]

        for i in range(n):
            board[i][self.Value(self.__variables[i])] = 1

        print()

        for line in board:

            for cell in line:

                character = "Q" if cell == 1 else "_"
                print(character, end=" ")

            print()

    def solution_count(self):
        """
        """

        return self.__solution_count
