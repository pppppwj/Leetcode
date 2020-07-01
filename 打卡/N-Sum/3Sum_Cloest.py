from typing import List


class Solution:

    # for sorted array
    def twoSumClosest(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        res = abs(target - nums[0] - nums[1])  # init res
        while i < j:
            tmp = target - nums[i] - nums[j]
            if tmp == 0:
                return 0
            elif tmp < 0:
                res = res if res <= abs(tmp) else abs(tmp)
                j -= 1
            else:
                res = res if res <= abs(tmp) else abs(tmp)
                i += 1
        return res

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()  # sort the array
        res = abs(target - nums[0] - nums[1] - nums[2])
        for i in range(len(nums) - 2):
            tmp = self.twoSumClosest(nums[i + 1 :], abs(target - nums[i]))
            res = res if res <= tmp else tmp
        return res

