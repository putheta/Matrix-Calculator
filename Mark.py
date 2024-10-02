import numpy as np

def select_argument_M():
    argumant_M = input("Argument Matrix? Y/N: ")
    if argumant_M == "y" or argumant_M == "Y":
        Start_M = "Yes this is argument matrix [A|b]!"
    elif argumant_M == "n" or argumant_M == "N":
        Start_M = "No this is only matrix A!"
    else:
        print("Please select Y/N")
        Start_M = None 
    return Start_M

def create_matrix():
    """Helper function to create a matrix from user input."""
    row_f = row
    col_f = col
    matrix = []
    
    print("Enter the matrix row by row:")
    for i in range(row):
        matrix_row = list(map(int, input(f"Enter elements for row {i+1} (space-separated): ").split()))
        if len(matrix_row) != col:
            print(f"Error: Row {i+1} must contain exactly {col} elements.")
            return None
        matrix.append(matrix_row)
    
    return np.array(matrix, dtype=float)

 
def elementary_op(A):
    row, col = A.shape
    for i in range(row): 
        if A[i, i] == 0:
            print(f"Error: Zero pivot found at row {i+1}. Row swapping needed, but not implemented.")
            return None
        
        for j in range(i + 1, row): 
            E = np.eye(row) 
            factor = -(A[j, i] / A[i, i]) 
            E[j, i] = factor
            print(f"Elementary Matrix for eliminating A[{j+1},{i+1}]:\n{E}\n")
            A = E.dot(A)
            print(f"Matrix after applying elementary operation:\n{A}\n")
    
    print("Final Upper Triangular Matrix:")
    print(f"{A}\n")
    return A

def rref(A):
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
    return A

# Example usage:
print("Hello I am Elementary Matrix!")

response = select_argument_M()
    
if response : 
    print(f"User selected: {response}")
    row = int(input("Input row numbers: "))
    col = int(input("Input column numbers: "))
    A = create_matrix()
    if A is not None: 
        print("\nOriginal Matrix:")
        print(f"{A} \n") 
        A = elementary_op(A)
        if A is not None:
            rref(A)
    

