#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0 
    i= 0
    while i<len(arr):
        if (arr[i]==i+1):    
            i+=1
            continue
        arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]
        count+=1            

    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

