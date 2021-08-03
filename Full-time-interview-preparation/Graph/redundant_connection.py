from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.parents = [-1 for _ in range(len(edges)+1)]
        for u,v in edges:
            if not self.union(u,v):
                return [u,v]
            
            
    def find(self, x):
        while self.parents[x] > 0:
            x = self.parents[x]
        
        return x
    
    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        if x_parent == y_parent:
            return False
        else:
            self.parents[x_parent] = y_parent
            return True
    