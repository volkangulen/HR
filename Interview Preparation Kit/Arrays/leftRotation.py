#!/bin/python

import math
import os
import random
import re
import sys
import Queue

# Complete the rotLeft function below.
def rotLeft(a, d):
    length = len(a)
    if(d==length):
        return a
    if(d>length/2):
         return rotateRight(a,length-d,length)
    return rotateLeft(a,d,length)
    
def rotateLeft(a,d,length):
    lst =[]
    for i in range(d):
        lst.append(a[(-i)%length])
    for i in range(length):
        lst.append(a[(-i-d)%length])
        a[(-i-d)%length] =lst.pop(0)
            
    return a

def rotateRight(a,d,length):
    lst =[]
    for i in range(d):
        lst.append(a[(i)%length])
    for i in range(length):
        lst.append(a[(i+d)%length])
        a[(i+d)%length] =lst.pop(0)
            
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

