class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        self.inorder_dfs(root, arr)
        return arr[k-1]
    def inorder_dfs(self, root, arr):
        if root:
            left = self.inorder_dfs(root.left, arr)
            arr.append(root.val)
            right = self.inorder_dfs(root.right, arr)
