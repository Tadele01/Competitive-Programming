from collections import defaultdict
from typing import List
class Solution: 
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for x, y in richer:
            graph[y].append(x)
        
        result, cache = [0 for _ in range(len(quiet))], {}
        for i in range(len(result)):
            result[i] = self.dfs(i, graph, quiet, cache)[1]
            
        return result
    
    def dfs(self, start, graph, quiet, cache):
        if start in cache:
            return cache[start]
        
        min_quiet, idx = quiet[start], start
        for neigh in graph[start]:
            neigh_quiet, neigh_idx = self.dfs(neigh, graph, quiet, cache)
            if neigh_quiet < min_quiet:
                min_quiet = neigh_quiet
                idx = neigh_idx
        
        cache[start] = (min_quiet, idx)
        
        return (min_quiet, idx)