class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        '''
            -for every node we change its left and right
            -our base case is when we encounter None node
            subproblem
                accept a node and change it left to right and vise versa
                
                for every right and left do the same
        ''' 
        arr = [root]
        self.invert_helper(root, arr)
        return arr[0]
    def invert_helper(self, root, arr):
        if root:
            if root.left is None and root.right is None:
                return 
            else:
                root.left, root.right = root.right, root.left
                self.invert_helper(root.left, arr)
                self.invert_helper(root.right, arr)
        else:
            return