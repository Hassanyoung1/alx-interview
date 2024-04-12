#!/usr/bin/python3

"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
"""


import sys

def is_valid(chessboard, row, col, N):
    # Check if placing a queen at (row, col) is valid
    for i in range(row):
        # Check the column
        if chessboard[i][col] == 'Q':
            return False
        # Check upper-left diagonal
        if abs(col - (row - i)) == abs(col - row) == abs(i - row):
            return False
        # Check upper-right diagonal
        if col + (row - i) < N and chessboard[i][col + (row - i)] == 'Q':
            return False
    return True

def place_queens(chessboard, row, N):
    if row == N:
        # All queens are successfully placed
        print_solution(chessboard)
        return

    for col in range(N):
        if is_valid(chessboard, row, col, N):
            chessboard[row][col] = 'Q'  # Place queen
            place_queens(chessboard, row + 1, N)  # Recur for next row
            chessboard[row][col] = '.'  # Backtrack

def print_solution(chessboard):
    # Print the positions of queens in the format [row, col]
    solution = []
    for row in range(len(chessboard)):
        for col in range(len(chessboard[row])):
            if chessboard[row][col] == 'Q':
                solution.append([row, col])
    print(solution)

def nqueens(N):
    N = int(N)
    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    chessboard = [['.' for _ in range(N)] for _ in range(N)]  # Initialize empty board
    place_queens(chessboard, 0, N)  # Start placing queens from the first row

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python filename.py N", file=sys.stderr)
        sys.exit(1)

    nqueens(sys.argv[1])
