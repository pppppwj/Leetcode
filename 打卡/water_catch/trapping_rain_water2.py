from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        visited = [[0] * n for _ in range(m)]
        dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)}  # up,down,left,right
        res = 0
        # boundary setting (ignore four coners)
        visited[0][0] = visited[-1][0] = visited[-1][-1] = visited[0][-1] = 1
        heap = []  # height , row, col
        for i in range(1, n - 1):
            heap.append((heightMap[0][i], 0, i))
            heap.append((heightMap[-1][i], m - 1, i))
            visited[0][i] = visited[-1][i] = 1
        for j in range(1, m - 1):
            heap.append((heightMap[j][0], j, 0))
            heap.append((heightMap[j][-1], j, n - 1))
            visited[j][0] = visited[j][-1] = 1
        heapq.heapify(heap)
        while heap:
            h, rr, cc = heapq.heappop(heap)
            for d in dirs:
                r = rr + d[0]
                c = cc + d[1]
                if 0 < r and r < m - 1 and 0 < c and c < n - 1 and not visited[r][c]:
                    visited[r][c] = 1
                    if h > heightMap[r][c]:
                        res += h - heightMap[r][c]
                        heapq.heappush(heap, (h, r, c))
                    else:
                        heapq.heappush(heap, (heightMap[r][c], r, c))
        return res
