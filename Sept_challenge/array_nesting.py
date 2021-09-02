from typing import List
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        nodes, max_len = set(), 1
        for i in range(len(nums)):
            if i not in nodes:
                max_len = max(max_len, self.dfs(i, nums, nodes))
        
        return max_len
    
    def dfs(self, i, nums, nodes):
        cur = nums[i]
        if cur in nodes:
            return 0
        
        nodes.add(cur)
        return 1 + self.dfs(cur, nums, nodes)
                
            
        