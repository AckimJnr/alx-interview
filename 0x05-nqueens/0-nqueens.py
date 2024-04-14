#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    Args:
        board: list of integers
        row: integer0-nqueens.py
        col: integer
    """
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i] == j:
            return False

    return True


def solve_n_queens(n):
    """
    Solve the n queens puzzle
    Args:
        n: integer
    """
    def helper(row, board):
        """
        Helper function to solve n queens
        Args:
            row: integer
            board: list of integers
        """
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                helper(row + 1, board)
                board[row] = -1

    solutions = []
    board = [-1] * n
    helper(0, board)
    return solutions


if __name__ == "__main__":
    """
    Parse command line arguments
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(N)
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])
