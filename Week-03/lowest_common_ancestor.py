class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowest_common_ancestor(self, root, p, q):
        parent_val = root.val
        p_val = p.val
        q_val = q.val
        if p_val > parent_val and q_val > parent_val:
            return self.lowest_common_ancestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowest_common_ancestor(root.left, p, q)
        else:
            return root