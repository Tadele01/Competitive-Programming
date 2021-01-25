class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
        
    def maxDepthIterative(self, root:TreeNode)->int:
        if not root:
            return 0    
        max_height = 1
        stack = [(root, 1)]
        while stack:
            root, depth = stack.pop()
            if not root.left and not root.right:
                max_height = max(max_height, depth)
            if root.left:
                stack.append((root.left, depth+1))
            if root.right:
                stack.append((root.right, depth+1))
           
        return max_height