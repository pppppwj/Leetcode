from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # Case 1 : k < 0
        if k < 0:
            return 0

        cnt = 0
        aux = {}  # empty dict   nums :: cntOfNums
        for i in range(len(nums)):
            if nums[i] in aux:
                aux[nums[i]] += 1
            else:
                aux[nums[i]] = 1

        # Case 2 :: k = 0
        if k == 0:
            for cntOfNums in aux.values():
                if cntOfNums > 1:
                    cnt += 1
        else:  # Case 3 :: k > 0
            for num in aux.keys():
                if num + k in aux:
                    cnt += 1
        return cnt

