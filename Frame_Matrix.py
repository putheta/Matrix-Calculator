import numpy as np

row = int(input("Input row numbers: "))
col = int(input("Input column numbers: "))

def row_operation(E, A, i, j, scalar):
    """Perform row operation on matrix A and update elementary matrix E.
    Arguments:
    E -- current elementary matrix
    A -- matrix to be operated on
    i -- row to be changed
    j -- row used for operation
    scalar -- multiplier for the row operation (A[i] = A[i] - scalar * A[j])
    """
    E[i] -= scalar * E[j]
    A[i] -= scalar * A[j]

def swap_rows(E, A, i, j):
    """Swap two rows in both matrix A and the elementary matrix E."""
    E[[i, j]] = E[[j, i]]
    A[[i, j]] = A[[j, i]]

def rref(A):
    """Find the RREF of a matrix using elementary matrices."""
    num_rows, num_cols = A.shape
    E = np.eye(num_rows)  # Start with the identity matrix as the elementary matrix
    
    lead = 0  # Leading pivot
    for r in range(num_rows):
        if lead >= num_cols:
            return A, E
        i = r
        # Find the pivot (non-zero element) and swap rows if necessary
        while A[i, lead] == 0:
            i += 1
            if i == num_rows:
                i = r
                lead += 1
                if lead == num_cols:
                    return A, E
        swap_rows(E, A, i, r)
        
        # Scale the row to make the pivot equal to 1
        pivot = A[r, lead]
        A[r] /= pivot
        E[r] /= pivot
        
        # Eliminate all entries in the current pivot column, except for the pivot itself
        for i in range(num_rows):
            if i != r:
                scalar = A[i, lead]
                row_operation(E, A, i, r, scalar)
        
        lead += 1  # Move to the next column
    
    return A, E

def create_matrix():
    """Helper function to create a matrix from user input."""
    
    # Initialize an empty matrix
    matrix = []
    
    # Loop to take input for each row
    print("Enter the matrix row by row:")
    for i in range(row):
        matrix_row = list(map(int, input(f"Enter elements for row {i + 1} (space-separated): ").split()))
        if len(matrix_row) != col:
            print(f"Error: Row {i + 1} must contain exactly {col} elements.")
            return None
        matrix.append(matrix_row)
    
    return np.array(matrix, dtype=float)

# Example usage:
A = create_matrix()
if A is not None:
    print("\nOriginal Matrix:")
    print(A)
    
    rref_matrix, E = rref(A)
    
    print("\nRREF Matrix:")
    print(rref_matrix)
    
    # Use len instead of row for correct indexing
    print("\nLast element of the first row of the RREF Matrix:")
    print(rref_matrix[0][len(rref_matrix[0]) - 1])
    
    print("\nElementary Matrix (for transformation):")
    print(E)
