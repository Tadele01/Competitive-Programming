class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root and not root.children:
            return 1
        max_height, counter = [0], [0]
        self.find_max_height(root, max_height, counter)
        return max_height[0]
    
    def find_max_height(self, root, max_height, counter):
        if not root:
            return 
        counter[0] +=1
        for child in root.children:
            self.find_max_height(child, max_height, counter)
            max_height[0] = max(max_height[0], counter[0])
            counter[0] -= 1
        