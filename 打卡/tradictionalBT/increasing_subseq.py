from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = {()}
        for _ in range(len(nums)):
            n = nums.pop(0)
            res |= {old + (n,) for old in res if not old or n >= old[-1]}
        return [r for r in res if len(r) > 1]

