# https://www.hackerrank.com/challenges/lisa-workbook/problem

def workbook(n, k, arr):
    # Write your code here
    page=1
    r=0
    q=0
    count=0
    for i in range(0,n):
        for j in range(1,arr[i]+1):
            if j==page:
                count+=1
            if j%k==0 or j==arr[i]:
                page+=1
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
