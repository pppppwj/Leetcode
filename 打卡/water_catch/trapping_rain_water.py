from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0
        bar = 0
        h = 0
        while l < r:
            res += (r-l)*(min(height[r],height[l])-h)
            h = min(height[r],height[l])
            while l<r and height[l]<=h:
                bar += height[l]
                l+=1
            while l<r and height[r]<=h:
                bar += height[r]
                r-=1
        return res - bar 
