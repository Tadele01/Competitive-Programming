# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#       self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        found = self.root_finder(root, val)
        if found:
            sub_array = []
            data = self.traverse(found, sub_array)[0]
            return data
        return None
    def root_finder(self, root, val):
        while root:
            if root.val == val:
                return root
            elif root.val >= val:
                return self.root_finder(root.left, val)
            elif root.val < val:
                return self.root_finder(root.right, val)
        return None
    def traverse(self, root, sub_tree):
        if root:
            sub_tree.append(root)
            self.traverse(root.left, sub_tree)
            self.traverse(root.right, sub_tree)
        return sub_tree