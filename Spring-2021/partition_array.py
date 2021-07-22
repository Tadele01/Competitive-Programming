from typing import List
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        min_elts = [float('inf')]
        for i in range(len(nums)-1, 0, -1):
            min_elts.append(min(nums[i], min_elts[-1]))
        
        left = 1
        min_elts, max_elt = list(reversed(min_elts)), nums[0]
        for i in range(1, len(nums)):
            if min_elts[i-1] >= max_elt:
                return left 
            max_elt = max(max_elt, nums[i])
            left += 1
        
        return left