from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # build an non-decreasing stack
        # store index
        stack = [-1]
        res = 0  # return value
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                res = (
                    res
                    if res >= heights[index] * (i - stack[-1] - 1)
                    else heights[index] * (i - stack[-1] - 1)
                )
            stack.append(i)
        while stack[-1] != -1:
            index = stack.pop()
            res = (
                res
                if res >= heights[index] * (len(heights) - stack[-1] - 1)
                else heights[index] * (len(heights) - stack[-1] - 1)
            )
        return res
