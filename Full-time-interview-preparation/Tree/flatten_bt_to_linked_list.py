# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return root
        
        preorder = []
        self.preorder_traverse(root, preorder)
        root.left = None
        cur_node, parent = root, root
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            cur_node.right = node
            cur_node = node
        
        return parent
        
        
    def preorder_traverse(self, root, preorder):
        if not root:
            return
        preorder.append(root.val)
        self.preorder_traverse(root.left, preorder)
        self.preorder_traverse(root.right, preorder)