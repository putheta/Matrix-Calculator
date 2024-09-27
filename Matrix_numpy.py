import numpy as np

#----------------------------------------------------------#
row = int(input("Row:"))
col = int(input("Col:"))

#----------------------------------------------------------#
def create(row, col):
    return np.random.randint(1, 10, size=(row, col))

def show(x):
    print(x, '\n')

def identity(row, col):
    return np.eye(min(row, col))  # Creates an identity matrix of appropriate size

def find_pivot(matrix):
    pivots = []
    for i in range(min(len(matrix), len(matrix[0]))):
        pivots.append(matrix[i, i])
    return pivots

def zero(shape):
    return np.zeros(shape)

def multiply(a, b):
    return np.dot(a, b)

def gaussian(matrix):
    pivoted_matrix = np.copy(matrix)
    row, col = matrix.shape
    for i in range(min(row, col)):
        pivot = matrix[i, i]
        if pivot != 0:
            for j in range(i + 1, row):
                factor = matrix[j, i] / pivot
                pivoted_matrix[j] = matrix[j] - factor * matrix[i]
    return pivoted_matrix

def gauss_jordan(matrix):
    reduced_matrix = np.copy(matrix)
    row, col = matrix.shape
    for i in range(min(row, col)):
        pivot = matrix[i, i]
        if pivot != 0:
            reduced_matrix[i] = matrix[i] / pivot
            for j in range(row):
                if i != j:
                    factor = matrix[j, i]
                    reduced_matrix[j] = matrix[j] - factor * reduced_matrix[i]
    return reduced_matrix

#----------------------------------------------------------#
main = create(row, col)
show(main)
show(identity(row, col))

# Row Echelon Form (REF)
ref_matrix = gaussian(main)
print("REF : ")
show(ref_matrix)

# Reduced Row Echelon Form (RREF)
rref_matrix = gauss_jordan(ref_matrix)
print("RREF : ")
show(rref_matrix)
