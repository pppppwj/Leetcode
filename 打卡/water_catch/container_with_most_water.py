from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l <= r:
            res = (
                res
                if res >= (r - l) * min(height[l], height[r])
                else (r - l) * min(height[l], height[r])
            )
            if height[l] < height[r]:
                tmp = height[l]
                while l <= r and height[l] <= tmp:
                    l += 1
            else:
                tmp = height[r]
                while l <= r and height[r] <= tmp:
                    r -= 1
        return res

