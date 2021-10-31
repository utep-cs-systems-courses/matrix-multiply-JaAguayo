#!/usr/bin/env python3
from matrixUtils import *
import time
import pymp

#Jared Aguayo, Part 1 Lab1 Matrix Multiply

#multiplies the 2 matrices by using for loops
def matrixMulti(matrix1,matrix2):
    
    #sets of the result matrix
    multi_result = genMatrix(len(matrix1),0)

    #timing algorithm
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    #rows of matrix 1
    for i in range(len(matrix1)): 
        #columns of matrix 2
        for j in range(len(matrix2[0])): 
            #rows of matrix 2
            for k in range(len(matrix2)): 
                multi_result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    elasped_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-start_time
    format_time = '{:.10f}'.format(elasped_time)

    #return the result of matrix and time it took to compute
    return multi_result,format_time

#New algorithm to multiply two matrices 
def matrixMultiBlocked(matrix1, matrix2):
    tile_size = 16
    #set of result matrix
    output = genMatrix(len(matrix1),0)

    #getting time to compute
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    for kk in range (0,len(matrix1),tile_size):
        for jj in range(0,len(matrix1),tile_size):
            for i in range (len(matrix1)):
                j_end_val = jj + tile_size
                for j in range(0,jj,j_end_val):
                    k_end_val = kk + tile_size
                    sum = output[i][j]
                    for k in range(0,kk,k_end_val):
                        sum = sum + matrix1[i][k] * matrix2[k][j]
                        output[i][j] = sum
                        
    elasped_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-start_time
    format_time = '{:.10f}'.format(elasped_time)

    #return matrix and time it took to compute 
    return output,format_time

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
    for i in range(15):
        for j in range(15):
            print(result[i][j], end = " ")
            
    print("\nTime to compute: Test 3 (Large matrices size 500, values 5 and 7)", comp_time)

    matrix1 = genMatrix(20,5)
    matrix2 = genMatrix(20,7)

    result, comp_time = matrixMultiBlocked(matrix1,matrix2)
    for r in result:
        print(r)
    print("Time to compute: Test 4 (Large matrices size 20, values 5 and 7)", comp_time)

if __name__ == '__main__':
    test()
    
