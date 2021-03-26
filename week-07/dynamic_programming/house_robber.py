from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_rob = 0
        for i in range(len(nums)):
            max_val = 0
            if i-2 >= 0:
                max_val = max(max_val, nums[i-2])
            if i-3 >= 0:
                max_val = max(max_val, nums[i-3])
            nums[i] += max_val
        
        return max(nums[-1], nums[-2])