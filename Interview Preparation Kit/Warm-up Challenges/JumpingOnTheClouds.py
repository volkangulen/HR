#!/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumpCount = 0
    arrLen = len(c)
    index = 1
    while(index < arrLen):
        if(index != arrLen-1 and c[index+1]):
            if(c[index]):
                break
            else:
                jumpCount += 1
                index += 1
        else:
            jumpCount += 1
            index += 2

    return jumpCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

