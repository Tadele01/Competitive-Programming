from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.result = []
        self.dfs(root, targetSum, [])
        return self.result
    
    def dfs(self, node, target, path):
        if not node:
            return
        if not node.left and not node.right:
            path.append(node.val)
            if sum(path) == target:
                self.result.append(path.copy())
                path.pop()
        
        if node.left:
            self.dfs(node.left, target, path+[node.val])
        if node.right:
            self.dfs(node.right, target, path+[node.val])