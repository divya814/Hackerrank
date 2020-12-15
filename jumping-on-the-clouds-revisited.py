# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c, k):
    e=100
    i=k%n
    e-=c[0]*2 + 1
    while i>0:
        e-=c[i]*2 + 1
        i=(i+k)%n
    return e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
