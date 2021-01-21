# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum_ = [0]
        return self.traverse(root, low, high, sum_)[0]
    
    def traverse(self, root, low, high, sum_):
        if root:
            if low <= root.val and root.val <= high:
                sum_[0] += root.val
            self.traverse(root.left, low, high, sum_)
            self.traverse(root.right, low, high, sum_)
        return sum_