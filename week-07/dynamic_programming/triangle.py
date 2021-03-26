from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(triangle, 0, 0, memo)
    
    def dfs(self, triangle, r, c, memo):
        if r == len(triangle):
            return 0
        if (r, c) in memo:
            return memo[(r, c)]
        left = self.dfs(triangle, r+1, c, memo)
        right = self.dfs(triangle, r+1, c+1, memo)
        cur = triangle[r][c]
        memo[(r, c)] = min(left, right) + cur
        return memo[(r, c)]