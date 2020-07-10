from typing import List
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = r = 0
        start = end = -1
        tmp = 0
        while r<len(nums):
            tmp += nums[r]
            if tmp>=s:
                while(l<=r and tmp>=s):
                    tmp -= nums[l]
                    l+=1
                l-=1
                tmp += nums[l]
                if start==-1 or end-start>r-l:
                    start,end = l,r
            r+=1
        return end-start+1 if start!=-1 else 0