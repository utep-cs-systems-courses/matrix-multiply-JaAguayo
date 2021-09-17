Jared Aguayo - Lab1 Part 1 and 2 Matrix Multiply adding Parallelism 
Part 1
The Program is a Matrix multiplier that takes either generated matrices or matrices from the files within the directory of the source code. 

The set test matrices are there to run the program, you can run the program in the IDE since there is a main or move to the directory where the source code is and type "python3 matrixMultiply.py" in the console to run it.

You can alter the matrices in the text files named, matrix1.txt and matrix2.txt. They must follow the format of the matrices already inputed in those files and the text files must be in the same directory as the source code.

There is a function in main calling a utlity function that can have the vaules altered in that function to change the size of the generated matrix and the values in the list from there, but they are set for testing.

I had a problem with the taking the times for the computations since the time
library is only for UNIX I haven't downloaded the VM yet so I coded this so
far on windows VScode, so I had to use the timeit library to get the times
which may need to be replaced once I download the VM

I have a bug where I cannot get the new algorithm to work so far, so I am
trying to work with the algorithm to try to figure it out, it will print out
the far left corner with one multiplication of it and the rest of the matrix
will be full of zeros. 

It took around 2 hours to complete this program 

There are tests taking times from different size matrices when multiplying them 

Part2
To begin I ran into a problem while making the function parallel that the
shared list I was using wasn't allowing the results to be stored until I
switches to shared.array to fix my problem.

There are no current known bugs in the parallel program

It took me a few hours only because I spent most of my time trying to make it
work with shared.list when switching to shared.array immediately made it run
correctly.

Using 1 thread
using a 50x50 matrix the time was: 0.3125

Using 2 threads
using a 50x50 matrix the time was: 0.1896

Using 4 threads
using a 50x50 matrix the time was: 0.0710

Using 8 threads
using a 50x50 matrix the time was: 0.0711

Using 16 threads
using a 50x50 matrix the time was: 0.1112

So to being the program runs on one thread which ends up being the slowest
since none of the word is split among other threads. Moving to 2 threads cut
the time in half and moving to 4 cut the time of using 2 in half since the
work was being split more and there were CPUs to take on the work. Then when 8
threads were used even though the work was split, the overhead from forming
the threads led to no performance difference and I tested 16 to show the
slower time and 16 threads ended up being almost as slow as 2 threads since
the overhead for that many threads was not worth the little work it took to do
amongst all those threads.

cpuInfo.sh Program (also a text file with the information)
model name	: AMD Ryzen 5 5600X 6-Core Processor
      4      36     192
