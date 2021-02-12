class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def all_possible_fbt(self, n:int)->list(TreeNode):
        result = []
        if n == 1:
            result.append(TreeNode(0))
        n -= 1
        for i in range(1, n, 2):
            left = self.all_possible_fbt(i)
            right = self.all_possible_fbt(n-i)
            for left_node in left:
                for right_node in right:
                    root = TreeNode(0)
                    root.left = left_node
                    root.right = right_node
                    result.append(root)
        return result
