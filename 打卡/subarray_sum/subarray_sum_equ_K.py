from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k) -> int:
        sum_cnt = {0:1}
        tmp = 0
        cnt = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if tmp-k in sum_cnt:
                cnt += sum_cnt[tmp-k]
            
            if tmp in sum_cnt:
                sum_cnt[tmp] += 1
            else:
                sum_cnt[tmp] = 1
        return cnt