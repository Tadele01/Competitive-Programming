from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = max(len(nums1), len(nums2))
        num_row , num_col = n, n
        
        dp = [[0 for _ in range(num_col)] for _ in range(num_row)]
        max_length = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    diag = dp[i-1][j-1] if i-1 >= 0 and j-1 >= 0 else 0
                    dp[i][j] += 1 + diag
                    max_length = max(max_length, dp[i][j])
            
        return max_length
        