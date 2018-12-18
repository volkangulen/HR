#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    count = 0
    l = len(q)
    # for i in q:
    #     if i>q.index(i)+3:
    #         print "Too chaotic"
    #         return
    swapped = False
    for i in range(l):
        for j in range(0,l-i-1):
            if(q[j]>j+3):
                print "Too chaotic"
                return
            if(q[j]>q[j+1]):
                count+=1
                swapped=True
                q[j],q[j+1]=q[j+1],q[j]
        if(swapped):
            swapped = False
        else:
            break
            

    print(count)

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

