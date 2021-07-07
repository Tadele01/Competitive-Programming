from heapq import heappush, heappop
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap, counter = [(matrix[0][0], 0, 0)], 1
        num_row, num_col, visited = len(matrix), len(matrix[0]), set()
        
        while min_heap:
            val, i, j = heappop(min_heap)
            for x, y in [(0, 1), (1, 0)]:
                new_r, new_c = i+x, j+y
                if 0<= new_r < num_row and 0<= new_c < num_col and (new_r, new_c) not in visited:
                    heappush(min_heap, (matrix[new_r][new_c], new_r, new_c))
                    visited.add((new_r, new_c))
            
            if counter == k:
                return val
            
            counter += 1
        