class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root:TreeNode, val:int) -> TreeNode:
        if root is None:
            new_node = TreeNode(val=val)
            return new_node
        self.insert(root, val)
        return root
    
    def insert(self, root, val):
        if root:
            if root.val > val:
                next_node = root.left
                if next_node is None:
                    new_node = TreeNode(val = val)
                    root.left = new_node
                    return
                self.insert(root.left, val)
            if root.val < val:
                next_node = root.right
                if next_node is None:
                    new_node = TreeNode(val = val)
                    root.right = new_node
                    return
                self.insert(root.right, val)
    