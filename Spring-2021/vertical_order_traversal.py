from collections import defaultdict, deque
from heapq import heappush, heappop
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        queue, min_heap, result = deque([(root, 0, 0)]), [(0, 0, root.val)], []
        while queue:
            for i in range(len(queue)):
                node, row, col = queue.popleft()
                if node.left:
                    queue.append((node.left, row+1, col-1))
                    heappush(min_heap, (col-1, row+1, node.left.val))
                if node.right:
                    queue.append((node.right, row+1, col+1))
                    heappush(min_heap, (col+1, row+1, node.right.val))
            
        cur_col, cur_row, val = heappop(min_heap)
        same_col = [val]
        while min_heap:
            col, row, val = heappop(min_heap)
            if col != cur_col:
                result.append(same_col)
                same_col = [val]
                cur_col = col
            else:
                same_col.append(val)
        result.append(same_col)
        return result
        