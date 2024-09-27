import math
import numpy as np
import copy

main = []
#----------------------------------------------------------#
row = int(input("Row: "))
col = int(input("Col: "))

#----------------------------------------------------------#
def create(row, col):
    for i in range(row):
        lst = []
        print(f"Enter values for row {i + 1} (space-separated):")
        values = input().split()
        for j in range(col):
            if j < len(values):
                lst.append(int(values[j]))  # แปลงค่าจาก string เป็น int
            else:
                lst.append(0)  # ถ้าจำนวนค่าที่ป้อนไม่พอ ให้เติมเป็น 0
        main.append(lst)

def show(x):
    for row in range(len(x)):
        print(x[row])
    print('\n')

def identity():
    temp = copy.deepcopy(main)
    for row in range(len(main)):
        for col in range(len(main[row])):
            if col == row:
                temp[row][col] = 1
            else:
                temp[row][col] = 0
    return temp

def find_pivot(x):
    pivot = []
    for row in range(len(x)):
        for col in range(len(x[row])):
            try:
                if (identity())[row][col] == 1:
                    pivot.append(x[row][col])
            except:
                pass
    return (pivot)

def zero():
    x = copy.deepcopy(main)
    for row in range(len(x)):
        for col in range(len(x[row])):
            x[row][col] = 0
    return x

def multiply(a, b):
    answer = zero()
    for row in range(len(a)):
        for col in range(len(b[0])):
            for coll in range(len(a[0])):
                answer[row][col] += round(a[row][coll] * b[coll][col], 2)

    return (answer)

def Gaussian(main):
    answer = copy.deepcopy(identity())
    for row in range(len(main)):
        for col in range(len(main[row])):
            if identity()[row][col] == 1:
                break
            if main[row][col] != 0 and identity()[row][col] == 0:
                answer[row][col] = (-1) * (main[row][col] / find_pivot(main)[col])
                break
    return answer

def Gauss_J(main):
    answer = copy.deepcopy(identity())
    for row in range(len(main)):
        for col in range(len(main[row])):
            if identity()[col][row] == 1:
                break
            if main[col][row] != 0 and identity()[col][row] == 0:
                answer[col][row] = (-1) * (main[col][row] / find_pivot(main)[row])
                break
    return answer

def normalize_pivot(matrix):
    """Ensure that pivot elements are 1 by dividing rows by their pivot."""
    for i in range(min(len(matrix), len(matrix[0]))):
        if matrix[i][i] != 0:
            pivot = matrix[i][i]
            for j in range(len(matrix[i])):
                matrix[i][j] /= pivot
    return matrix

#----------------------------------------------------------#

create(row, col)
show(main)

# Row Echelon Form
for i in range(row):
    multiply(Gaussian(main), main)
    main = copy.deepcopy(multiply(Gaussian(main), main))
print("REF: ")
show(main)

# Normalize pivot to 1
main = normalize_pivot(main)
print("Normalized REF (with pivot as 1):")
show(main)

# Reduced Row Echelon Form
for row in range(len(identity())):
    for col in range(len(identity()[row])):
        if row != col and main[row][col] != 0:
            multiply(Gauss_J(main), main)
            main = copy.deepcopy(multiply(Gauss_J(main), main))

# Normalize pivot to 1 (for RREF)
main = normalize_pivot(main)
print("RREF with normalized pivot:")
show(main)
