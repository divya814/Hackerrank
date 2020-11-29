# Find it on- https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# My Code
def kangaroo(x1, v1, x2, v2):
    # If the starting point of 1 kangaroo is less than its speed must be greater than the other, for both of them to meet
    if (x2-x1)*(v2-v1)<0 and (x2-x1)%(v2-v1)==0:
        return "YES"
    else:
        return "NO"
    
# Given
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
