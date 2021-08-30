#!/usr/bin/env python3
from matrixUtils import *

#multiplies the 2 matrices by using for loops
def matrixMulti(matrix1,matrix2):

    multi_result = createResultList(matrix1,matrix2)

    #rows of matrix 1
    for i in range(len(matrix1)): 
        #columns of matrix 2
        for j in range(len(matrix2[0])): 
            #rows of matrix 2
            for k in range(len(matrix2)): 
                multi_result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return multi_result

#Creates a list of the correct dimensions of the final product and fills with 0s
def createResultList(matrix1,matrix2):
    rows=[]
    if (len(matrix1) >= len(matrix2)):
        row = len(matrix1)
    else:
        row = len(matrix2)
    
    if (len(matrix1[0]) >= len(matrix2[0])):
        col = len(matrix1[0])
    else:
        col = len(matrix2[0])

    for x in range(0,row):
        columns = []
        for y in range (0,col):
            columns.append(0)
        rows.append(columns)
    
    return rows

if __name__ == '__main__':
    matrix1 = readFromFile("matrix1.txt")
    print(matrix1)

    matrix2 = readFromFile("matrix2.txt")
    print(len(matrix2[0]))

    result = matrixMulti(matrix1,matrix2)
    print(result)




