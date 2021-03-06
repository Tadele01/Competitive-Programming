class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p:TreeNode, q:TreeNode)-> bool:

        p_arr = []
        q_arr = []
        self.traverse(p, p_arr)
        self.traverse(q, q_arr)

        if len(p_arr) == len(q_arr):
            count = 0
            for i in range(len(p_arr)):
                if p_arr[i] == q_arr[i]:
                    count +=1
            if count == len(p_arr):
                return True
        else:
            return False

    def traverse(self, root, arr):
        if root:
            self.traverse(root.left, arr)
            arr.append(root.val)
            self.traverse(root.right, arr)

        arr.append(None)
    def isSameTree2(self, p, q):
        if p and q:
            if p.val != q.val:
                return False
            else:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                return left and right
            
        if (p and not q) or (not p and q):
            return False
        return True