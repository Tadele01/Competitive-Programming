from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        queue = deque([root])
        res = deque([(root.val, None, None)])
        sum_ = 0
        while queue:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                result = res.popleft()
                if not result[2] == None:
                    if result[2] % 2 == 0:
                        sum_ += front.val
                if front.left:
                    queue.append(front.left)
                    new_family = (front.left.val, result[0], result[1])
                    res.append(new_family)
                if front.right:
                    queue.append(front.right)
                    new_family = (front.right.val, result[0], result[1])
                    res.append(new_family)
                    
        return sum_
                