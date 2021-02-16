from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        res = [root.val]
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                front = queue.popleft()
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            if queue:
                res.append(sum([i.val for i in queue])/len(queue))
        return res