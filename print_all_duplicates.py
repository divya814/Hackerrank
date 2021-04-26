# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

n=256
def fill(s,count):
    for i in s:
        count[ord(i)]+=1
    return count
    
def dup(s):
    c=[0]*n
    c=fill(s,c)
    k=0
    
    for i in c:
        if int(i)>1:
            print(chr(k)+"="+str(i))
        k+=1
    
s="geekforgeeek"
dup(s)
