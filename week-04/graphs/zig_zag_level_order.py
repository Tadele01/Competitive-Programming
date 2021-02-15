from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        level = 0
        res = [[root.val]]
        while queue:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            level +=1
            if not queue:
                break
            if level % 2 == 0:
                arr = [i.val for i in queue]
                res.append(arr)
            else:
                arr = [queue[i].val for i in range(len(queue)-1, -1, -1)]
                res.append(arr)
        return res                