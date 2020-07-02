from heapq import heappush, heapreplace


class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []  # right one
        self.maxheap = []  # left one

    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0:
            self.minheap.append(num)
        elif len(self.maxheap) == 0:
            if self.minheap[0] >= num:
                self.maxheap.append(-num)
            else:
                self.maxheap.append(-self.minheap[0])
                self.minheap[0] = num
        else:
            min_minheap = self.minheap[0]
            max_maxheap = -self.maxheap[0]
            mid = num
            if min_minheap < num:
                mid = heapreplace(self.minheap, num)
            elif max_maxheap > num:
                mid = -heapreplace(self.maxheap, -num)

            if len(self.minheap) == len(self.maxheap):
                heappush(self.minheap, mid)
            else:
                heappush(self.maxheap, -mid)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0]) / 2
        else:
            return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
