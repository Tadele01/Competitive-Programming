class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_ max_ = -float('inf'), float('inf')
        return self.traverse_inorder(root, min_, max_)   
    def traverse_inorder(self, root, min_, max_):
        if not root:
            return True
        if root.val <= min_ or root.val >= max_:
            return False
        left = self.traverse_inorder(root.left, min_, root.val)
        right = self.traverse_inorder(root.right, root.val, max_)
        return left and right