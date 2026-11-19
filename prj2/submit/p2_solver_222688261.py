# ENG 1112 - Project 2 - starter file
# Write solve() and residual() yourself. Loops and conditionals over lists only.
# No numpy.linalg.solve, no matrix inverse, inside solve().


PRECISION = 3  # number of digits printed for each unknown
TOLERANCE = 1e-9  # a pivot smaller than this counts as zero (see the guide, Part D)
# 222688261
# P = 39.1 N downward at joint D
# Q = 9.8 N downward at joint C

def read_system(file_name):
    file = open(file_name)
    line = file.readline()
    number_of_equations = int(line)
    matrix = []
    for _ in range(number_of_equations):
        line = file.readline()
        row = []
        parts = line.split()  # split() with no argument: any number of spaces, no stray "\n"
        for part in parts:
            row += [float(part)]
        matrix += [row]
    line = file.readline()
    labels = line.split()
    file.close()
    return number_of_equations, matrix, labels


def copy(matrix):
    copy_of_matrix = []
    for row in matrix:
        copy_of_row = []
        for element in row:
            copy_of_row += [element]
        copy_of_matrix += [copy_of_row]
    return copy_of_matrix


def solve(number_of_equations, matrix):
    # Renamed k to pivot_column and 
    # p to pivot_row so their roles are clear.
    working_matrix = copy(matrix)
    # forward elimination with partial pivoting
    for pivot_column in range(number_of_equations - 1):
        # Renamed i to row: row is the row currently being checked.
        pivot_row = pivot_column
        for row in range(pivot_column + 1, number_of_equations):
            if abs(working_matrix[row][pivot_column]) > abs(
                working_matrix[pivot_row][pivot_column]
            ):
                pivot_row = row

        if abs(working_matrix[pivot_row][pivot_column]) < TOLERANCE:
            return None

        if pivot_row != pivot_column:
            temporary = working_matrix[pivot_column]
            working_matrix[pivot_column] = working_matrix[pivot_row]
            working_matrix[pivot_row] = temporary

        # Eliminate the values below the pivot in this column.
        for row in range(pivot_column + 1, number_of_equations):
            multiplier = (
                working_matrix[row][pivot_column]
                / working_matrix[pivot_column][pivot_column]
            )
            # Renamed j to column; column includes the right-hand-side column.
            for column in range(pivot_column, number_of_equations + 1):
                working_matrix[row][column] -= (
                    multiplier * working_matrix[pivot_column][column]
                )

    last_pivot = number_of_equations - 1
    if abs(working_matrix[last_pivot][last_pivot]) < TOLERANCE:
        return None

    # back substitution, from the last row up
    solution = [0.0] * number_of_equations
    # Renamed i to row and j to column in back substitution.
    # Work upward: later solution values are already known.
    for row in range(number_of_equations - 1, -1, -1):
        total = 0.0
        for column in range(row + 1, number_of_equations):
            total += working_matrix[row][column] * solution[column]
        solution[row] = (
            working_matrix[row][number_of_equations] - total
        ) / working_matrix[row][row]
    return solution


def residual(number_of_equations, matrix, solution):
    residual = 0.0
    # largest |row_i . solution - b_i| over the rows of the original matrix, using a nested loop
    for row in range(number_of_equations):
        row_total = 0.0
        for column in range(number_of_equations):
            row_total += matrix[row][column] * solution[column]
        row_residual = abs(row_total - matrix[row][number_of_equations])
        if row_residual > residual:
            residual = row_residual
    return residual


# here the main code starts
print("System file: ", end="")
file_name = input()
number_of_equations, matrix, labels = read_system(file_name)
solution = solve(number_of_equations, matrix)
if solution is None:
    print("Singular system")
else:
    for i in range(len(labels)):
        print(labels[i], round(solution[i], PRECISION))
    print("max residual", residual(number_of_equations, matrix, solution))
