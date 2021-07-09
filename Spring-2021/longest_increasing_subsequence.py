class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest, cache = 0, {}
        for i in range(len(nums)):
            longest = max(longest, self.dfs(nums, i, cache))
            
        return longest
    
    def dfs(self, nums, i, cache):
        if i in cache:
            return cache[i]
        
        max_increasing = 0
        for j in range(i, len(nums)):
            if nums[i] < nums[j]:
                max_increasing = max(max_increasing, self.dfs(nums, j, cache))

        cache[i] = max_increasing + 1
        return max_increasing + 1