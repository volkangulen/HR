#!/bin/python

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = 0
    maxSum = -sys.maxint
    
    for i in range(4):
        for j in range(4):
            for pI in range(3):
                for pJ in range(3):
                    if(pI == 1 and pJ in [0,2]):
                        continue;
                    sum += arr[i + pI][j + pJ]
            maxSum=max(sum,maxSum)
            sum = 0
    
    return maxSum
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

