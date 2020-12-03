# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    a=len(arr)
    b=0
    c=0
    for i in range(a):
        for j in range(a):
            if i==j:
                b+=arr[i][j]
            if i+j==a-1:
                c+=arr[i][j]
    return abs(b-c)
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
