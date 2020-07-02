from typing import List
from collections import Counter
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Approach 2 : Two Heaps (Lazy Removal)
        if k == 1 or len(nums) <= 1:
            return nums  # special case

        # init two heap
        init = sorted(nums[:k])
        max_heap = []
        for i in init[: (1 + k) // 2][::-1]:
            max_heap.append(-i)
        min_heap = init[(1 + k) // 2 :]

        if k % 2 == 0:
            ISEVEN = True
        else:
            ISEVEN = False

        medians = []
        if ISEVEN:
            medians.append((min_heap[0] - max_heap[0]) / 2)
        else:
            medians.append(-max_heap[0])

        pop_nums = Counter()  # hash map to store invalid nums
        for i in range(len(nums) - k):
            out = nums[i]
            in_ = nums[i + k]

            if out <= -max_heap[0]:
                balance = -1
            else:
                balance = 1

            pop_nums[out] += 1

            if in_ <= -max_heap[0]:
                heapq.heappush(max_heap, -in_)
                balance += 1
            else:
                heapq.heappush(min_heap, in_)
                balance -= 1

            if balance < 0:
                heapq.heappush(max_heap, -heapq.heappop(min_heap))
            elif balance > 0:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))

            while pop_nums[-max_heap[0]]:
                pop_nums[-max_heap[0]] -= 1
                heapq.heappop(max_heap)
            while pop_nums[min_heap[0]]:
                pop_nums[min_heap[0]] -= 1
                heapq.heappop(min_heap)

            if ISEVEN:
                medians.append((min_heap[0] - max_heap[0]) / 2)
            else:
                medians.append(-max_heap[0])

        return medians


if __name__ == "__main__":
    # test case
    nums = [1, 3, -2, -3, 5, 3, 6, 7]
    k = 3

    sol = Solution()
    print(sol.medianSlidingWindow(nums, k))

