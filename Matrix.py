import math
import random
import copy
3
main = []
b = []
#----------------------------------------------------------#
row = int(input("Row:"))
#col = row

col = int(input("Col:"))

#row = random.randint(1,9)
#col = random.randint(1,9)

#----------------------------------------------------------#
def create(row,col) :
    for i in range(row) :
        lst = []
        for i in range(col) :
            num = random.randint(1,9)
            lst.append(num)
        main.append(lst)

def show(x) :
    for row in range(len(x)) :
        print(x[row])
    print('\n')

def identity() :
    temp = copy.deepcopy(main)
    for row in range(len(main)) :
        for col in range(len(main[row])) :
            if col == row :
                temp[row][col] = 1 
            elif col+1>len(main) :
                temp[row].pop()
            else :
                temp[row][col] = 0
    return temp

def find_pivot(x) :
    pivot=[]
    for row in range(len(x)) :
        for col in range(len(x[row])) :
            try :
                if (identity())[row][col] == 1 :
                    pivot.append(x[row][col])
            except :
                pass
    return (pivot)

def zero() :
    x = copy.deepcopy(main)
    for row in range(len(x)) :
        for col in range(len(x[row])) :
            x[row][col] = 0
    return x 
            
def multiply(a,b) :
    answer = zero()
    for row in range(len(a)) :
        for col in range(len(b[0])) :
                for coll in range(len(a[0])) :
                    answer[row][col] += round(a[row][coll] * b[coll][col],2)
    
    return (answer)

def Gaussian(main) :
    answer = copy.deepcopy(identity())
    for row in range(len(main)) :
        for col in range(len(main[row])) :
            if identity()[row][col] == 1 :
                break
            if main[row][col]!=0 and identity()[row][col]==0 :
                answer[row][col] = (-1)*(main[row][col]/find_pivot(main)[col])
                break
    return answer
def Gauss_J(main) :
    answer = copy.deepcopy(identity())
    for row in range(len(main)) :
        for col in range(len(main[row])) :
            if identity()[col][row] == 1 :
                break
            if main[col][row]!=0 and identity()[col][row]==0 :
                answer[col][row] = (-1)*(main[col][row]/find_pivot(main)[row])
                break
    return answer

#----------------------------------------------------------#

create(row,col)
show(main)
#print("b",b)
show(identity())

#Row Echelon Form
for i in range(row) :
    multiply(Gaussian(main),main)
    main = copy.deepcopy(multiply(Gaussian(main),main))
print("REF : ")
show(main)

#for i in range(row+1) :
#    multiply(Gauss_J(main),main)
#    main = copy.deepcopy(multiply(Gauss_J(main),main))
#print("RREF : ")
#show(main)

for row in range(len(identity())) :
    for col in range(len(identity()[row])) :
        if row!=col and main[row][col] != 0  :
                multiply(Gauss_J(main),main)
                main = copy.deepcopy(multiply(Gauss_J(main),main))
            
            
print("RREF")       
show(main)