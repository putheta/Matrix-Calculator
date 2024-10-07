import numpy as np

def create_matrix(row, col):
    matrix = []
    print("Enter the matrix row by row:")
    for i in range(row):
        matrix_row = list(map(float, input(f"Enter elements for row {i+1} (space-separated): ").split()))
        if len(matrix_row) != col:
            print(f"Error: Row {i+1} must contain exactly {col} elements.")
            return None
        matrix.append(matrix_row)
    return np.array(matrix)

def swap_rows(A, row1, row2):
    """Swaps two rows in the matrix A."""
    A[[row1, row2]] = A[[row2, row1]]
    print(f"Swapped row {row1+1} with row {row2+1}:\n{A}\n")
    return A

def elementary_op(A):
    row, col = A.shape
    for i in range(row):
        if A[i, i] == 0:
            for j in range(i + 1, row):
                if A[j, i] != 0:
                    A = swap_rows(A, i, j)
                    break
            else:
                print(f"Warning: Cannot find a non-zero pivot for column {i+1}. Free variables may exist.")
                continue
        
        for j in range(i + 1, row): 
            if A[j, i] != 0:  
                E = np.eye(row)
                factor = -(A[j, i] / A[i, i])
                E[j, i] = factor
                A = E.dot(A)
    
    print("Final Upper Triangular Matrix:")
    print(f"{A}\n")
    return A

def rrefm(A):
    row, col = A.shape
    for i in range(row): 
        if A[i, i] != 1:
            E = np.eye(row)
            factor = 1 / A[i, i]
            E[i, i] = factor
            print(f"Elementary Matrix for scaling row {i+1} to make pivot 1:\n{E}\n")
            A = E.dot(A)
            print(f"Matrix after scaling row {i+1}:\n{A}\n")
        for j in range(row):
            if j != i:
                E = np.eye(row)
                factor = -A[j, i]
                E[j, i] = factor
                print(f"Elementary Matrix for eliminating A[{j+1},{i+1}]:\n{E}\n")
                A = E.dot(A)
                print(f"Matrix after eliminating A[{j+1},{i+1}]:\n{A}\n")

    print("Final RREF Matrix:")
    print(f"{A}\n")

def rref(A):
    row, col = A.shape

    for i in range(row):
        if np.all(A[i, :-1] == 0) and A[i, -1] != 0: 
            print("The system is inconsistent.")
            print(f"Inconsistency found in row {i+1}: {A[i]}")
            return None 

   
    for i in range(row):
        if A[i, i] != 1 and A[i, i] != 0:  
            A[i] = A[i] / A[i, i]  
            print(f"Scaled row {i+1} to make pivot 1:\n{A}\n")
        for j in range(row):
            if j != i and A[j, i] != 0:  
                factor = A[j, i]
                A[j] = A[j] - factor * A[i]
                print(f"Eliminated A[{j+1},{i+1}] using row {i+1}:\n{A}\n")
    
    print("Final RREF Matrix:")
    print(f"{A}\n")

   
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
        print("Free variables exist:")
        for j in free_vars:
            print(f"x{j+1} is free, setting x{j+1} = 1")
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

    #Solution
    print("Solution:")
    for i, x in enumerate(solution):
        print(f"x{i+1} = {x}")  

    return A

#Main
print("Hello, I am Elementary Matrix!")
argumant_M = input("Argument Matrix? Y/N: ")

if argumant_M.lower() == "y":
    Start_M = "Yes, this is an augmented matrix [A|b]!"
    print(f"User selected: {Start_M}")
    row = int(input("Input row numbers: "))
    col = int(input("Input column numbers (including the augmented column): "))
    A = create_matrix(row, col)
    if A is not None:
        print("\nOriginal Matrix:")
        print(f"{A} \n")
        A = elementary_op(A)
        if A is not None:
            rref(A)
elif argumant_M.lower() == "n":
    Start_M = "No, this is only matrix A!"
    print(f"User selected: {Start_M}")
    row = int(input("Input row numbers: "))
    col = int(input("Input column numbers: "))
    A = create_matrix(row, col)
    if A is not None:
        print("\nOriginal Matrix:")
        print(f"{A} \n")
        A = elementary_op(A)
        if A is not None:
            rrefm(A)
else:
    print("Please select Y/N")
# test