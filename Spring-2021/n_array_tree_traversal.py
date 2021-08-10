class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
from collections import deque
from typing import List
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        result, queue = [], deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            
            result.append(level)
        
        return result