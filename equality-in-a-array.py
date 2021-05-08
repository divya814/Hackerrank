# https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    # Write your code here
    l=len(arr)
    m=max(arr)
    a=[0]*(m+1)
    for i in range(l):
        a[arr[i]]+=1
    
    m=999   # minimum frequency of element
    s=sum(a)
    c=0
    for i in range(1,len(a)):
        c=0
        c=s-a[i]
        if c<m:
            m=c
    return m
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
