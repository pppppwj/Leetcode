from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # insert index
        i,j = 0,1
        while j<len(nums):
            if nums[j] != nums[i]:
                i+=1
                nums[i]=nums[j]
            j+=1
        return i+1

         