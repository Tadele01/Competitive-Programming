from collections import defaultdict
from typing import List
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        not_allowed, graph = defaultdict(list), defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        result = [1 for _ in range(n)]
        
        for garden in range(1, n+1):
            for i in range(1, 5):
                if i not in not_allowed[garden]:
                    result[garden-1] = i
                    for neigh in graph[garden]:
                        not_allowed[neigh].append(i)
                    break
        
        return result   