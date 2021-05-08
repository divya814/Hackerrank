# https://www.hackerrank.com/challenges/acm-icpc-team/problem

from itertools import combinations
n,k = map(int,input().split())
teams = [list(map(int,list(input()))) for i in range(n)]
sums = [sum([x[0] or x[1] for x in list(zip(*i))]) for i in combinations(teams,2)]
print(max(sums),sums.count(max(sums)),sep='\n')



# another code- Brute Force approach - giving TLE in one test case 
def acmTeam(topic):
    # Write your code here
    l=len(topic)
    t=len(topic[0])
    a=[]    
    for i in range(l):
        for k in range(i+1,l):
            c=0            
            for j in range(t):
                if topic[i][j]=='1' or topic[k][j]=='1':
                    c+=1
            a.append(c)
    m=max(a)
    ans=[m,a.count(m)]
    return ans
               
