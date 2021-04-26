# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        n={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        a=0
        i=0
        while i<len(s)-1:
            if n[s[i]]>=n[s[i+1]]:
                a+=n[s[i]]
                i+=1
            elif n[s[i]]<n[s[i+1]]:
                a+=n[s[i+1]]-n[s[i]]
                i+=2
        if i<len(s):
            a+=n[s[i]]
        return a
