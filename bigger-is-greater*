# https://www.hackerrank.com/challenges/bigger-is-greater/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    a=list(w)
    i=len(a)-1
    while i>0 and a[i-1]>=a[i]:
        i-=1
    
    if i<=0:
        return "no answer"
    
    j=len(a)-1
    while a[i-1]>=a[j]:
        j-=1
    a[i-1],a[j]=a[j],a[i-1]
    
    a[i:]=a[len(a)-1 : i-1 : -1]
    return "".join(a)
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
