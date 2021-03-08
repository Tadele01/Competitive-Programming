from heapq import heappop, heappush
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        min_heap = []
        for row in range(R):
            for col in range(C):
                ans = abs(row-r0) + abs(col-c0)
                heappush(min_heap, (ans, row, col))
        res = []
        while min_heap:
            d = heappop(min_heap)
            res.append(d[1:])
        return res
                