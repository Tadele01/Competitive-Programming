from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {x:i for i, x in enumerate(nums)}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in indices:
                if diff == nums[i] and i != indices[diff]:
                    return [i, indices[diff]]
                            
                elif diff != nums[i]:
                    return [i, indices[diff]]