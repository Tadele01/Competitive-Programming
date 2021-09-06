from collections import defaultdict
from typing import List
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(node, parent, depth):
            ans = 1
            for neib in graph[node]:
                if neib != parent:
                    ans += dfs(neib, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans
        
        def dfs2(node, parent, w):
            ans[node] = w
            for neib in graph[node]:
                if neib != parent:
                    dfs2(neib, node, w + n- 2*weights[neib])
        
        weights, depths, ans = [0]*n, [0]*n, [0]*n
        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))
        
        return ans
        
        