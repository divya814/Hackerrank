# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
# ord() gives the unicode for the character
# eg. ord("a")=97

def designerPdfViewer(h, word):
    width=len(word)
    a=[]
    for i in word:
        s=ord(i)-ord('a')
        a.append(h[s])
    return max(a)*width

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
