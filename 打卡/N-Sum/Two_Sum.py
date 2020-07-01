from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}  # empty dict
        for i in range(len(nums)):
            if nums[i] in aux:
                return i, aux[nums[i]]
            else:
                aux[target - nums[i]] = i
