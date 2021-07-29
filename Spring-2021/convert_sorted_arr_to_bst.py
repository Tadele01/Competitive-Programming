from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_bst(nums)

    def build_bst(self, nums):
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.build_bst(nums[:mid])
        root.right = self.build_bst(nums[mid+1:])
        
        return root