from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_leaf(self, root:TreeNode)->bool:
        return root.left == None and root.right == None
    def minimum_depth_of_bt(self, root:TreeNode)->int:
        if self.is_leaf(root):
            return 0
        queue = deque()
        level = 1
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                if self.is_leaf(front):
                    return level
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            level +=1
        return level
        
        
