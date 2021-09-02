#!/usr/bin/env python3
from matrixUtils import *
import timeit

#multiplies the 2 matrices by using for loops
def matrixMulti(matrix1,matrix2):

    multi_result = createResultList(matrix1,matrix2)

    start_time = timeit.default_timer()
    #rows of matrix 1
    for i in range(len(matrix1)): 
        #columns of matrix 2
        for j in range(len(matrix2[0])): 
            #rows of matrix 2
            for k in range(len(matrix2)): 
                multi_result[i][j] += matrix1[i][k] * matrix2[k][j]
    elasped_time = timeit.default_timer()-start_time
    format_time = '{:.10f}'.format(elasped_time)
    
    return multi_result,format_time

#New algorithm to multiply two matrices 
def matrixMultiBlocked(matrix1, matrix2):
    tile_size = 16 
    output = createResultList(matrix1, matrix2)

    for kk in range (0,len(matrix1),tile_size):
        for jj in range(0,len(matrix1),tile_size):
            for i in range (0,len(matrix1)):
                j_end_val = jj + tile_size
                for j in range(0,jj,j_end_val):
                    k_end_val = kk + tile_size
                    sum = output[i][j]
                    for k in range(0,kk,k_end_val):
                        sum = sum + matrix1[i][k] * matrix2[k][j]
                    output[i][j] = sum
                    print(output)

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

#test fucntion to run some multiplies 
def test():
    matrix1 = readFromFile("matrix1.txt")

    matrix2 = readFromFile("matrix2.txt")

    result,comp_time = matrixMulti(matrix1,matrix2)
    for r in result:
        print(r)
    print("Time to compute: Test 1 (two small matrices from file)", comp_time)

    matrix1 = genMatrix(600,5)
    matrix2 = genMatrix(600,3)

    result,comp_time = matrixMulti(matrix1, matrix2)   
    print("Time to compute: Test 2 (Large matrices size 600, values 5 and 3)", comp_time)

    matrix1 = genMatrix(500,5)
    matrix2 = genMatrix(500,7)

    result,comp_time = matrixMulti(matrix1, matrix2)
    print("Time to compute: Test 3 (Lared matrices size 500, values 5 and 7)", comp_time)


if __name__ == '__main__':
    test()
    """
    matrix1 = genMatrix(20,5)
    matrix2 = genMatrix(20,7)

    matrixMultiBlocked(matrix1,matrix2)

    """


