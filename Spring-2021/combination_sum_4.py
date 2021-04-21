class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        return self.dfs(nums, target, cache)
    
    def dfs(self, nums, running_diff, cache):
        if running_diff in cache:
            return cache[running_diff]
        
        if running_diff == 0:
            return 1
        if running_diff < 0:
            return 0
        
        count = 0
        for num in nums:
            count += self.dfs(nums, running_diff - num, cache)
            
        cache[running_diff] = count
        return cache[running_diff]