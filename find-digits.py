# https://www.hackerrank.com/challenges/find-digits/problem

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    c=0
    for x in str(n):
        if x!="0" and n%int(x)==0:
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
