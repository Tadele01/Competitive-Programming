from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.dfs(1, n)
    
    def dfs(self, min_elt, max_elt):
        if min_elt > max_elt:
            return [None]
        
        if min_elt == max_elt:
            return [TreeNode(min_elt)]
        
        result = []
    
        for i in range(min_elt, max_elt+1):
            left = self.dfs(min_elt, i-1) 
            right = self.dfs(i+1, max_elt)
            for l in left:
                for r in right:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    result.append(node)
            
                    
        return result 
            
        