# https://www.hackerrank.com/challenges/electronics-shop/problem

import os
import sys

#
# Complete the getMoneySpent function below.
# Mine
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    h=[]
    for i in keyboards:
        for j in drives:
            if i+j<=b:               
                h.append(i+j)
    if not h:
        return -1
    else:
        return max(h)
            
# given
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
