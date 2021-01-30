from heapq import heappop, heappush, heapify
class Solution:
    def lastStoneWeight(self, stones) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(-1*stone)
        heapify(max_heap)
        while max_heap:
            if len(max_heap) == 1:
                return abs(max_heap[0])
            first_max = abs(heappop(max_heap))
            second_max = abs(heappop(max_heap))
            if first_max == second_max:
                continue
            diff = first_max - second_max
            heappush(max_heap, -1*diff)
        return 0