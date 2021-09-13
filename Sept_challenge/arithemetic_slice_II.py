from typing import List
from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:  
        subsequence = 0
        cache = [defaultdict(int) for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                cache[i][diff] += cache[j][diff] + 1
                subsequence += cache[j][diff]
                
        return subsequence