# ENG 1112 - linsolve.py - Gaussian elimination, the same solve() as in Project 2
# This file holds functions only, so another program can import it:
#     from linsolve import solve
# You may replace copy() and solve() with your own from Project 2. Paste the functions and the
# TOLERANCE line only. Leave out the main code at the bottom of your Project 2 file: Python runs
# everything in a file when the file is imported, so that code would stop and ask for a system file.

TOLERANCE = 1e-9  # a pivot smaller than this counts as zero


def copy(matrix):
    copy_of_matrix = []
    for row in matrix:
        copy_of_row = []
        for element in row:
            copy_of_row += [element]
        copy_of_matrix += [copy_of_row]
    return copy_of_matrix


def solve(number_of_equations, matrix):
    # matrix is the augmented matrix: number_of_equations rows, each with the coefficients
    # followed by the right-hand side. Returns the solution as a list, or None when the
    # system is singular.
    copy_of_matrix = copy(matrix)  # work on a copy, the caller keeps the original
    # forward elimination with partial pivoting
    for k in range(number_of_equations):
        p = k
        for i in range(k + 1, number_of_equations):
            if abs(copy_of_matrix[i][k]) > abs(copy_of_matrix[p][k]):
                p = i
        if abs(copy_of_matrix[p][k]) < TOLERANCE:
            return None
        if p != k:
            row = copy_of_matrix[k]
            copy_of_matrix[k] = copy_of_matrix[p]
            copy_of_matrix[p] = row
        for i in range(k + 1, number_of_equations):
            multiplier = copy_of_matrix[i][k] / copy_of_matrix[k][k]
            for j in range(k, number_of_equations + 1):
                copy_of_matrix[i][j] -= multiplier * copy_of_matrix[k][j]
    # back substitution, from the last row up
    solution = [0.0] * number_of_equations
    for i in range(number_of_equations - 1, -1, -1):
        total = copy_of_matrix[i][number_of_equations]
        for j in range(i + 1, number_of_equations):
            total -= copy_of_matrix[i][j] * solution[j]
        solution[i] = total / copy_of_matrix[i][i]
    return solution
