class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_symmetric(self, root):
        if root is None:
            return True
        else:
            return self.check_symmetric(root.left, root.right)
    
    def check_symmetric(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            left_most = self.check_symmetric(left.left, right.right)
            right_most = self.check_symmetric(left.right, right.left)
            return left_most and right_most
        else:
            return False