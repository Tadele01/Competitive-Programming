from typing import List
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        half = (sum(piles) // 2) + 1
        return True if (self.dfs(piles, 0, len(piles)-1, {}) >= half) else False
        
    def dfs(self, piles, i, j, cache):
        if i > j:
            return  0
        if (i, j) in cache:
            return cache[(i, j)]
        
        max_gain =  max(max(piles[i], piles[j]) + self.dfs(piles, i+1, j-1, cache), \
                        self.dfs(piles, i+2, j, cache), \
                        self.dfs(piles, i, j-2, cache))
        
        cache[(i, j)] = max_gain
        return max_gain
