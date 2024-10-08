import numpy as np

def create_matrix(row, col):
    matrix = []
    print("Enter the matrix row by row:")
    for i in range(row):
        while True:
            try:
                # Prompt for input and convert to float
                matrix_row = list(map(float, input(f"Enter elements for row {i+1} (space-separated): ").split()))
                if len(matrix_row) != col:
                    print(f"Error: Row {i+1} must contain exactly {col} elements. Please try again.")
                else:
                    matrix.append(matrix_row)
                    break  # Exit loop on successful input
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
    return np.array(matrix)

def print_matrix(A, step_desc):
    """Prints the current state of the matrix with a description."""
    print(f"{step_desc}:\n{A}\n")

def elementary_op(A):
    row, col = A.shape
    for i in range(row):
        # Check for a zero pivot
        if A[i, i] == 0:
            for j in range(i + 1, row):
                if A[j, i] != 0:  # Find a row with a non-zero entry to swap
                    # Construct the elementary matrix for swapping
                    E = np.eye(row)
                    E[[i, j]] = E[[j, i]]
                    print(f"Elementary Matrix for swapping row {i+1} with row {j+1}:\n{E}\n")
                    A = E @ A
                    print_matrix(A, f"After swapping row {i+1} with row {j+1}")
                    break
            else:
                print(f"Warning: Column {i+1} has no non-zero pivot. Free variables may exist.")
                continue  # Move to the next column if no swap is possible
        
        # Scale the pivot row
        pivot = A[i, i]
        if pivot != 1:
            E = np.eye(row)
            E[i, i] = 1 / pivot
            print(f"Elementary Matrix for scaling row {i+1}:\n{E}\n")
            A = E @ A
            print_matrix(A, f"After scaling row {i+1}")

        # Eliminate below the pivot
        for j in range(i + 1, row): 
            if A[j, i] != 0:
                factor = -A[j, i]
                E = np.eye(row)
                E[j, i] = factor
                print(f"Elementary Matrix for eliminating A[{j+1},{i+1}]:\n{E}\n")
                A = E @ A
                print_matrix(A, f"After eliminating A[{j+1},{i+1}]")
    
    print("Final Upper Triangular Matrix:")
    print(A)
    return A

def rref(A):
    row, col = A.shape

    # Start from the last pivot and work upwards
    for i in range(row - 1, -1, -1):
        # Ensure pivot is 1
        pivot = A[i, i]
        if pivot != 1 and pivot != 0:
            E = np.eye(row)
            E[i, i] = 1 / pivot
            print(f"Elementary Matrix for scaling row {i+1}:\n{E}\n")
            A = E @ A
            print_matrix(A, f"After scaling row {i+1}")

        # Eliminate above the pivot
        for j in range(i):
            if A[j, i] != 0:
                factor = -A[j, i]
                E = np.eye(row)
                E[j, i] = factor
                print(f"Elementary Matrix for eliminating A[{j+1},{i+1}]:\n{E}\n")
                A = E @ A
                print_matrix(A, f"After eliminating A[{j+1},{i+1}]")

    print("Final RREF Matrix:")
    print(A)
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
            print(f"x{j+1} is free, setting x{j+1} = 1")
            solution[j] = 1
    
    # Substitute back to get the correct values
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
        print(f"x{i+1} = {x}")

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
        print(A)
        A = elementary_op(A)
        if A is not None:
            A = rref(A)
            if A is not None:
                solve_system(A)
elif argument_M.lower() == "n":
    Start_M = "No, this is only matrix A!"
    print(f"User selected: {Start_M}")
    row = int(input("Input row numbers: "))
    col = int(input("Input column numbers: "))
    A = create_matrix(row, col)
    if A is not None:
        print("\nOriginal Matrix:")
        print(A)
        A = elementary_op(A)
        if A is not None:
            A = rref(A)
else:
    print("Please select Y/N")
