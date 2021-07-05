class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.dfs(root, inorder)

        return self.build_bst(inorder, 0, len(inorder)-1)
    
    def build_bst(self, inorder, left, right):
        if left > right:
            return None
        
        index = left + ((right - left) // 2)
        new_root = TreeNode(inorder[index])
        new_root.left = self.build_bst(inorder, left, index-1)
        new_root.right = self.build_bst(inorder, index+1, right)
    
        return new_root

    def dfs(self, root, inorder):
        if not root:
            return
        
        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)
    
