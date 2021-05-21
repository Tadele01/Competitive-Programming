# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        dead_end = [-float('inf')]
        
        return max(self.dfs(root, dead_end), dead_end[0])
    
    def dfs(self, root, dead_end):
        if not root:
            return 0
        
        left = self.dfs(root.left, dead_end) 
        right = self.dfs(root.right, dead_end)
        
        max_path = max(left+root.val, right+root.val, root.val)
        
        dead_end[0] = max(dead_end[0], left+right+root.val, root.val, left+root.val, right+root.val)
        
        return max_path