from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or (root.left == None and root.right == None): 
            return True
        queue = deque()
        level = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                front = queue.popleft()
                (queue.append(front.left) or level.append(front.left)) if front.left else                              level.append(None)
                (queue.append(front.right) or level.append(front.right)) if front.right else                            level.append(None)
            while level:
                front_elt, rear_elt = level.popleft(), level.pop()
                if (front_elt == None and not rear_elt == None) or \
                    (rear_elt == None and not front_elt == None):
                    return False
                if front_elt == None and rear_elt == None:
                    continue
                elif front_elt.val != rear_elt.val:
                    return False
        return True