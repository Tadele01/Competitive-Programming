class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        arr = []
        self.traverse(root, arr)
        return arr

    def traverse(self, root, arr):
        if root:
            self.traverse(root.left, arr)
            self.traverse(root.right, arr)
            arr.append(root.val)

    
        
