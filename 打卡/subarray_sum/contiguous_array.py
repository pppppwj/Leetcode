from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        res = 0
        cnt = 0
        cnt_first_index = {0: 0}
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1

            if cnt in cnt_first_index:
                res = (
                    res
                    if res > i - cnt_first_index[cnt] + 1
                    else i - cnt_first_index[cnt] + 1
                )
            else:
                cnt_first_index[cnt] = i + 1
        return res
