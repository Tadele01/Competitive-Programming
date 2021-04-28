from heapq import heappop, heappush
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        min_heap = []
        for num in arr:
            diff = abs(num - x)
            heappush(min_heap, (diff, num))
            
        result = []
        for i in range(k):
            diff, num = heappop(min_heap)
            result.append(num)
            
        result.sort()
        return result