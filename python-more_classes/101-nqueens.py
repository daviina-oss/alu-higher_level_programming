#!/usr/bin/python3
"""Solve the N queens problem.

Usage: nqueens N
Prints every solution as a list of [row, column] pairs, one per line.
"""
import sys


def solve(n, row=0, cols=None):
    """Return every solution of the N queens problem by backtracking.

    Args:
        n: the size of the board.
        row: the row on which the next queen is placed.
        cols: the columns chosen so far, one per row already filled.
    """
    if cols is None:
        cols = []
    if row == n:
        return [[[r, c] for r, c in enumerate(cols)]]
    solutions = []
    for col in range(n):
        if all(col != c and abs(col - c) != row - r
               for r, c in enumerate(cols)):
            solutions += solve(n, row + 1, cols + [col])
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in solve(n):
        print(solution)
