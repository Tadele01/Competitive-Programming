class Solution:
    def maxDepth(self, s: str) -> int:
        d = {'(' : 1, ')' : -1}
        max_depth = depth = 0
        for c in s:
            depth += d.get(c, 0)
            max_depth = max(depth, max_depth)
        return max_depth