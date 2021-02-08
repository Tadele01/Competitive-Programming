class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        left, right = [], []
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            if preorder[i] < root.val:
                left.append(preorder[i])
            else:
                right.append(preorder[i])
        root.left = self.bstFromPreorder(left)
        root.right = self.bstFromPreorder(right)
        return root