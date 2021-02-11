class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.find_bottom(root)[1]
    
    def find_bottom(self, root:TreeNode)->tuple:
        if not root:
            return (0, None)
        left = self.find_bottom(root.left)
        right = self.find_bottom(root.right)
        if left[1] == None and right[1] == None:
            return (left[0]+1, root.val)
        return (left[0]+1, left[1]) if left[0] >= right[0] else (right[0]+1, right[1])