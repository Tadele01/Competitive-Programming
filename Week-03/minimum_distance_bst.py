class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = [-float('inf'), float('inf')]
        return self.in_order(root, prev)
    def in_order(self, root, prev):
        if not root:
            return
        self.in_order(root.left, prev)
        prev[1] = min(prev[1], root.val - prev[0])
        prev[0] = root.val
        self.in_order(root.right, prev)
        return prev[1]