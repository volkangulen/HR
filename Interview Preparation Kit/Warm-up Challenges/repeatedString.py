#!/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    sLen = len(s)
    remaining = n%sLen
    count = 0
    additionalCount = 0
    #a count in s
    for i in range(sLen):
        if(i==remaining):
            additionalCount = count
        if(s[i]=='a'):
            count += 1
        
        
    count *= n/sLen
    return count + additionalCount
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

