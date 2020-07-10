from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        TWICE = False
        while j<len(nums):
            if nums[j]==nums[i]:
                if not TWICE:
                    i+=1
                    nums[i]=nums[j]
                    TWICE = True
            else:
                TWICE = False
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1
            
