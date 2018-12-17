#!/bin/python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleyCount = 0
    level = 0
    for i in s:
        if(i == 'D'):
            level -= 1
        else:
            level += 1
            if(level == 0):
                valleyCount += 1
    return valleyCount
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    s = raw_input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

