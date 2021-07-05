# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = deque()
        self.dfs(root, self.queue)
    
    def next(self) -> int:
        if self.hasNext():
            return self.queue.popleft()

    def hasNext(self) -> bool:
        if self.queue:
            return True
        return False
    def dfs(self, root, queue):
        if not root:
            return
        self.dfs(root.left, queue)
        queue.append(root.val)
        self.dfs(root.right, queue)