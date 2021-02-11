class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

class Solution:
    def longest_univalue_path(self, root:TreeNode)->int:
        if not root:
            return 0
        return self.find_path(root)[1]
    def find_path(self, root:TreeNode)->tuple:
        if not root:
            return (0, 0, -1001)
        left = self.find_path(root.left)
        right = self.find_path(root.right)
        if root.val == left[2] and root.val == right[2]:
            local_max = max(left[0]+1, right[0]+1)
            global_max = max((left[0] + right[0]) + 2, left[1], right[1])
            return (local_max, global_max, root.val)
        elif root.val == left[2]:
            local_max = left[0] + 1
            global_max = max(local_max, left[1], right[1])
            return (local_max, global_max, root.val)
        elif root.val == right[2]:
            local_max = right[0] + 1
            global_max = max(local_max, right[1], left[1])
            return (local_max, global_max, root.val)
        return (0, max(left[1], right[1]), root.val)