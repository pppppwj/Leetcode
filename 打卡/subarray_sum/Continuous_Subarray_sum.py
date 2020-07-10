from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod_index = {0:-1}
        tmp=0
        for i in range(len(nums)):
            tmp += nums[i]
            if k!=0:
                tmp = tmp % k
            if tmp in mod_index:
                if i>mod_index[tmp]+1:
                    return True
            else:
                mod_index[tmp]=i        
        return False
