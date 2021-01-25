class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def mergeTrees(self, t1:TreeNode, t2:TreeNode) -> TreeNode:
        if t1 and t2:
            val = t1.val + t2.val
            node = TreeNode(val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 if t1 is not None else t2