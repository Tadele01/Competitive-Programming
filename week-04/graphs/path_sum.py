class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasSum(self, root:TreeNode, targetSum: int)->bool:
        summation = [0]
        return self.get_sum(root, targetSum, summation)
    def get_sum(self, root, targetSum):
        if not root:
            return
        summation[0] +=1
        left = self.get_sum(root.left, targetSum, summation)
        if summation[0] == targetSum and (not root.left and not root.right):
            return True
        right = self.get_sum(root.right, targetSum, summation)
        if summation[0] == targetSum and (not root.left and not root.right):
            return True
        summation[0] -= root.val
        return left or right