from heapq import heappop, heappush, heapify
class KthLargest:
    def __init__(self, k:int, nums:list)->int:
        nums = sorted(nums)
        self.min_heap = []
        for _ in range(k):
            if nums:
                heappush(self.min_heap, nums.pop())
        self.k = k
    def add(self, val:int)->int:
        if self.min_heap:
            if val > self.min_heap[0] and len(self.min_heap) == self.k:
                heappop(self.min_heap)
                heappush(self.min_heap, val)
            elif len(self.min_heap) < self.k:
                heappush(self.min_heap, val)
        else:
            heappush(self.min_heap, val)

        return self.min_heap[0]