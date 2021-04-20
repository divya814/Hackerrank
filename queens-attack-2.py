# https://www.hackerrank.com/challenges/queens-attack-2/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r,c, obstacles):
    s=set([(x,y) for x,y in obstacles])
    count=0
    m=[
        [1,-1],[1,0],[1,1],
        [0,-1],[0,1],
        [-1,-1],[-1,0],[-1,1]
        ]
        
    for i in m:
        x=r
        y=c
        while True:
            x+=i[0]
            y+=i[1]
            if x==0 or y==0 or x==n+1 or y==n+1:
                break
            if (x,y) in s:
                break
            count+=1        
    return count
    
""" Explanation in simpler code
def queensAttack(n, k, r_q, c_q, obstacles):
        count=0
        #up
        row=r_q+1
        col=c_q
        l=[row,col]
        while(row<=n):
            if(l in obstacles):
                break
            else:
                count=count+1
                row=row+1
                l=[row,col]
        
        #down
        
        row=r_q-1
        col=c_q
        l=[row,col]
        while(row>=1):
            if(l in obstacles):
                break
            else:
                count=count+1
                row=row-1
                l=[row,col]
        
        #left
        
        row=r_q
        col=c_q-1
        l=[row,col]
        while(col>=1):
            if(l in obstacles):
                break
            else:
                count=count+1
                col=col-1
                l=[row,col]
        
        #right
        
        row=r_q
        col=c_q+1
        l=[row,col]
        while(col<=n):
            if(l in obstacles):
                break
            else:
                count=count+1
                col=col+1
                l=[row,col]
        
        #upleft
        
        row=r_q+1
        col=c_q-1
        l=[row,col]
        while(col>=1 and row<=n):
            if(l in obstacles):
                break
            else:
                count=count+1
                col=col-1
                row=row+1
                l=[row,col]
       
        #upright
        
        row=r_q+1
        col=c_q+1
        l=[row,col]
        while(col<=n and row<=n):
            if(l in obstacles):
                break
            else:
                count=count+1
                col=col+1
                row=row+1
                l=[row,col]
        
        #downleft
        
        row=r_q-1
        col=c_q-1
        l=[row,col]
        while(col>=1 and row>=1):
            if(l in obstacles):
                break
            else:
                count=count+1
                col=col-1
                row=row-1
                l=[row,col]
        
        #downright
        row=r_q-1
        col=c_q+1
        l=[row,col]
        while(col<=n and row>=1):
            if(l in obstacles):
                break
            else:
                count=count+1
                col=col+1
                row=row-1
                l=[row,col]
        
        return count
"""

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
