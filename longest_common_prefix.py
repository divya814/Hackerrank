# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:      # strs = ["flower","flow","flight"]
        l=len(s)
        p=""
        if l==1:
            return s[0]
        
        first=s[0]
        for i in range(len(first)):
            for j in range(1,l):
                if i<len(s[j]):
                    if first[i]!=s[j][i]:
                        return p
                else:
                    return p
            p=p+first[i]
        
        return p
            
