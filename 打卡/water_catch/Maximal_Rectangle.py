from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        left = [0] * n
        right = [n] * n
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                    res = (
                        res
                        if res > height[j] * (right[j] - left[j])
                        else height[j] * (right[j] - left[j])
                    )
                else:
                    left[j] = 0
                    height[j] = 0
                    cur_left = j + 1

        return res
