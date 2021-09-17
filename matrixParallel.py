#!/usr/bin/env python3
from matrixUtils import *
import time
import pymp

#Jared Aguayo, Part 2 Lab 1 Parallel Matrix Multiply

#multiplies the 2 matrices by using for loops using Parallel
def matrixMultiParallel(matrix1,matrix2):
    
    #shared array for parallel 
    shared_multi_result = pymp.shared.array((len(matrix1),(len(matrix2[0]))),dtype='uint16')
    start_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    
    with pymp.Parallel() as p:
        print(f'number of threads: {p.thread_num} of {p.num_threads}')
        #rows of matrix 1, parallelize the rows of matrix 1
        for i in p.range(len(matrix1)): 
            #columns of matrix 2
            for j in range(len(matrix2[0])): 
                #rows of matrix 2
                for k in range(len(matrix2)):
                    shared_multi_result[i][j] +=  matrix1[i][k] * matrix2[k][j]
                    
    
        elasped_time = time.clock_gettime(time.CLOCK_MONOTONIC_RAW)-start_time
        format_time = '{:.10f}'.format(elasped_time)

    #return the result of matrix and time it took to compute
    return shared_multi_result,format_time

def main():
    #50x50 test times
    matrix1 = genMatrix(50,5)
    matrix2 = genMatrix(50,5)
    result,time = matrixMultiParallel(matrix1,matrix2)
    print(time)

    matrix1 = genMatrix(5,9)
    matrix2 = genMatrix(5,5)
    result,time = matrixMultiParallel(matrix1,matrix2)
    print(result)
    print('small test matrix to check for correct output size 5x5, time:',time)
    
if __name__ == '__main__':
    main()
