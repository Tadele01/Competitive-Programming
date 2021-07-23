class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        
        if not left and not right and root.val == 0:
            return None
        
        root.left = left
        root.right = right
        
        return root