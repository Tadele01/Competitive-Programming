from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        unique = set(nums)
        return True if target in unique else False