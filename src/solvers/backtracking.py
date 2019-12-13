"""
"""

from solvers.base import BaseSolver


class BacktrackingSolver(BaseSolver):
    """
    """

    def _is_safe_place(self, board, row, column):
        """
        """

        # Check Row on Left Side
        for i in range(column):
            if board[row][i] == 1:
                return False

        # Check Upper Diagonal on Left Side
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check Lower Diagonal on Left Side
        for i, j in zip(range(row, self._n, 1), range(column, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def _print_configuration(self, board):
        """
        """

        print()

        for line in board:

            for cell in line:

                character = "Q" if cell == 1 else "_"
                print(character, end=" ")

            print()

    def _backtrack(self, board, column):
        """
        """

        if column >= self._n:

            # It is a Solution

            self._solutions += 1

            if self._print_solutions:
                self._print_configuration(board)

            return

        for row in range(self._n):

            if self._is_safe_place(board, row, column):

                replicated_board = [
                    line[:] for line in board
                ]

                replicated_board[row][column] = 1

                self._backtrack(replicated_board, column + 1)

    def _solve(self):
        """
        """

        self._solutions = 0

        board = [
            [0 for _ in range(self._n)]
            for _ in range(self._n)
        ]

        self._backtrack(board, 0)

        return self._solutions
