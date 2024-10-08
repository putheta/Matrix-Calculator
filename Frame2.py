import numpy as np

def create_matrix(row, col):
    matrix = []
    print("Enter the matrix row by row:")
    for i in range(row):
        matrix_row = list(map(float, input(f"Enter elements for row {i + 1} (space-separated): ").split()))
        if len(matrix_row) != col:
            print(f"Error: Row {i + 1} must contain exactly {col} elements.")
            return None
        matrix.append(matrix_row)
    return np.array(matrix)

def print_elementary_matrix(E):
    print(E, "\n")

def swap_rows(A, row1, row2):
    """Swaps two rows in the matrix A."""
    A[[row1, row2]] = A[[row2, row1]]
    return A

def elementary_op(A):
    row, col = A.shape
    for i in range(row):
        # Check for a zero pivot
        if A[i, i] == 0:
            for j in range(i + 1, row):
                if A[j, i] != 0:  # Find a row with a non-zero entry to swap
                    print(f"Swapping row {i + 1} with row {j + 1} to avoid zero pivot.")
                    A = swap_rows(A, i, j)
                    break
            else:
                print(f"Warning: Column {i + 1} has no non-zero pivot. Free variables may exist.")
                continue  # Move to the next column if no swap is possible
        
        # Scale the pivot row
        E = np.eye(row)
        E[i, i] = 1 / A[i, i]
        print_elementary_matrix(E)
        A = E @ A  # Apply elementary matrix (scaling)
        
        # Eliminate below the pivot
        for j in range(i + 1, row):
            if A[j, i] != 0:
                factor = A[j, i]
                E = np.eye(row)
                E[j, i] = -factor
                print(f"Elementary Matrix for eliminating A[{j + 1}, {i + 1}]:")
                print_elementary_matrix(E)
                A = E @ A  # Apply elementary matrix (elimination)
    
    print("Final Upper Triangular Matrix:")
    print(A, "\n")
    return A

def rref(A):
    row, col = A.shape
    for i in range(row):
        if A[i, i] != 1:
            E = np.eye(row)
            factor = 1 / A[i, i]
            E[i, i] = factor
            print(f"Elementary Matrix for scaling row {i + 1} to make pivot 1:")
            print_elementary_matrix(E)
            A = E @ A  # Scale to make pivot 1
        
        for j in range(row):
            if j != i:
                E = np.eye(row)
                factor = -A[j, i]
                print(f"Elementary Matrix for eliminating A[{j + 1}, {i + 1}]:")
                E[j, i] = factor
                print_elementary_matrix(E)
                A = E @ A  # Eliminate other rows

    print("Final RREF Matrix:")
    print(A, "\n")
    return A

def solve_system(A):
    row, col = A.shape
    solution = np.zeros(col - 1)
    leading_cols = []

    for i in range(row):
        pivot_col = -1
        for j in range(col - 1):
            if A[i, j] == 1:
                pivot_col = j
                break
        
        if pivot_col >= 0:
            leading_cols.append(pivot_col)
            solution[pivot_col] = A[i, -1] 
    
    free_vars = [j for j in range(col - 1) if j not in leading_cols]
    
    if free_vars:
        print("Free variables exist. Setting them to arbitrary values.")
        for j in free_vars:
            print(f"x{j + 1} is free, setting x{j + 1} = 1")
            solution[j] = 1
    
    for i in range(row):
        pivot_col = -1
        for j in range(col - 1):
            if A[i, j] == 1:
                pivot_col = j
                break
        
        if pivot_col >= 0:
            rhs = A[i, -1]
            for j in range(col - 1):
                if j != pivot_col:
                    rhs -= A[i, j] * solution[j]
            solution[pivot_col] = rhs

    print("Solution:")
    for i, x in enumerate(solution):
        print(f"x{i + 1} = {x}")

# Main
print("Hello, I am Elementary Matrix!")
argument_M = input("Argument Matrix? Y/N: ")

if argument_M.lower() == "y":
    Start_M = "Yes, this is an augmented matrix [A|b]!"
    print(f"User selected: {Start_M}")
    row = int(input("Input row numbers: "))
    col = int(input("Input column numbers (including the augmented column): "))
    A = create_matrix(row, col)
    if A is not None:
        print("\nOriginal Matrix:")
        print(A, "\n")
        A = elementary_op(A)
        if A is not None:
            A_rref = rref(A)
            solve_system(A_rref)
elif argument_M.lower() == "n":
    Start_M = "No, this is only matrix A!"
    print(f"User selected: {Start_M}")
    row = int(input("Input row numbers: "))
    col = int(input("Input column numbers: "))
    A = create_matrix(row, col)
    if A is not None:
        print("\nOriginal Matrix:")
        print(A, "\n")
        A = elementary_op(A)
        if A is not None:
            A_rref = rref(A)
            solve_system(A_rref)
else:
    print("Please select Y/N")
