class Node:
    def __init__(self, val:int=0, left:Node=None, right:Node = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root:Node)->int:
        result = []
        self.dfs(root, result, [])
        return sum(result)

    def dfs(self, root, result, path):
        if not root:
            return 

        path.append(str(root.val))
        self.dfs(root.left, result, path)
        self.dfs(root.right, result, path)
        if not root.left and not root.right:
            val = int(''.join(path))
            result.append(val)
        path.pop()