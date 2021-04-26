# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1#

# This solution is of 0(n^2) complexity... that's why it gives TLE

class Solution:

    def longestPalin(self, a):
        l=len(a)
        n=a[0]
        for i in range(0,l):
            for j in range(i,l):
                b=a[i:j+1]
                c=b[::-1]
                if b==c:
                    m=b
                if len(m)>len(n):
                    n=m
        return n
