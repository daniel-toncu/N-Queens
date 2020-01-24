"""
"""

import sys

from solvers.backtracking import BacktrackingSolver
from solvers.backtracking_imp import BacktrackingImpSolver
from solvers.cp_sat import CpSatSolver


if __name__ == "__main__":
    """
    """

    print()

    if len(sys.argv) != 4:

        print(" Usage: python %s <solver> <board-size> <print-solutions>\n" %
              sys.argv[0])

        sys.exit()

    print_solutions = False

    if sys.argv[3].lower() in ["true", "1", "t", "y", "yes", "yeah", "yup", "certainly", "uh-huh"]:

        print_solutions = True

    try:

        board_size = int(sys.argv[2])

    except ValueError as e:

        print(" Error: Invalid Value for \"board-size\" parameter (\"%s\"): %s.\n" %
              (sys.argv[2], e))

        sys.exit()

    if sys.argv[1].lower() == "backtracking":

        print(" Solver: Backtracking")

        solver = BacktrackingSolver(board_size, print_solutions)

    if sys.argv[1].lower() == "backtracking-imp":

        print(" Solver: Backtracking-Imp")

        solver = BacktrackingImpSolver(board_size, print_solutions)

    elif sys.argv[1].lower() == "cp-sat":

        print(" Solver: CP-SAT")

        solver = CpSatSolver(board_size, print_solutions)

    else:

        print(" Error: Invalid Value for \"solver\" parameter (\"%s\")." %
              sys.argv[1])
        print(" Allowed Solvers: \"backtracking\" and \"cp-sat\".\n")

        sys.exit()

    print(" Board Size: %d" % board_size)
    print(" Print Solutions: %s" % print_solutions)

    print("\n===\n")

    (execution_time, found_solutions) = solver.solve()

    if print_solutions:
        print("\n===\n")

    print(" Found Solutions: %d." % found_solutions)
    print(" Execution Time: %f." % execution_time)

    print()
