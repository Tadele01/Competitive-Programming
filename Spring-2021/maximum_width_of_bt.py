from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque((root, 0))
        max_width = 0
        while queue:
            max_width = max(max_width, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                cur_node, idx = queue.popleft()
                if cur_node.left:
                    queue.append((cur_node.left, 2*(idx-1) + 1))
                if cur_node.right:
                    queue.append((cur_node.right, 2*(idx-1) + 2))



        return max_width