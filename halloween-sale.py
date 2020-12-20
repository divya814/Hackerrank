# https://www.hackerrank.com/challenges/halloween-sale/problem

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    c=0
    k,a=p,p
    while True:
        if k<=s:
            a-=d
            c+=1
            if a>=m:
                k+=a
            else:
                k+=m
        else:
            break
    return c
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
