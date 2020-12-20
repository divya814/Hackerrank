# https://www.hackerrank.com/challenges/minimum-distances/problem

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    c=[]
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                c.append(abs(i-j))
    if c==[]:
        return -1
    else:
        return min(c)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
