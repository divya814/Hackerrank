# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=len(h)-1
        left=0
        right=l
        area=0
        while left<right:
            if h[left]<h[right]:
                area=max(area,(right-left)*h[left])
                left+=1
            else:
                area=max(area,(right-left)*h[right])
                right-=1
        return area
        
        
