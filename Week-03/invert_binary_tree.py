class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
            -for every node we change its left and right
            -our base case is when we encounter None node
            subproblem
                accept a node and change it left to right and vise versa
                
                for every right and left do the same
        ''' 
        if root:
            if root.left is None and root.right is None:
                return root
            else:
                root.left, root.right = root.right, root.left
                self.invertTree(root.left)
                self.invertTree(root.right)
        return root
