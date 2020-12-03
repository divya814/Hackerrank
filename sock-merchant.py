# https://www.hackerrank.com/challenges/sock-merchant/problem

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    a=0
    # count function can be with sets to count frequency of elements
    for i in set(ar):
        # return 1 if ar.count(i)//2 is true
        a+= ar.count(i)//2
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
