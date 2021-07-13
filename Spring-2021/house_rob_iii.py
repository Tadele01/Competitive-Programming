from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        return self.dfs(root, False, {})
    
    def dfs(self, node, parent_robbed, cache):
        if not node:
            return 0
        if (node, parent_robbed) in cache:
            return cache[(node, parent_robbed)]
        
        if not node.left and not node.right:
            return (0, node.val)[not parent_robbed]
        
        l_rob = self.dfs(node.left, False, cache)
        r_rob = self.dfs(node.right, False, cache)
        max_elt = l_rob + r_rob
        
        if not parent_robbed:
            l_rob = self.dfs(node.left, True, cache)
            r_rob = self.dfs(node.right, True, cache)
            max_elt = max(max_elt, l_rob + r_rob + node.val)
        
        cache[(node, parent_robbed)] = max_elt
        
        return max_elt
            