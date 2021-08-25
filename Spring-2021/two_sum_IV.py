class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return self.dfs(root, set(), k)       
    
    def dfs(self, node, lookup, k):
        if not node: return False
        if k - node.val in lookup: return True
        
        lookup.add(node.val)
        return self.dfs(node.left, lookup, k) or self.dfs(node.right, lookup, k)