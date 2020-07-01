from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        aux = {}  # empty dict
        for i in range(len(nums)):
            if nums[i] in aux:
                return aux[nums[i]], i + 1  # unique diff
            else:
                aux[target - nums[i]] = i + 1

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while True:
            tmp = nums[i] + nums[j]
            if tmp == target:
                return i + 1, j + 1
            elif tmp > target:
                j -= 1
            else:
                i += 1
