from typing import List
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.parents = [parent]
        for k in range(1, 17):
            self.parents.append([])
            for node in range(n):
                p = self.parents[k-1][node]
                if p != -1:
                    p = self.parents[k-1][p]
                self.parents[k].append(p)
        
    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(17):
            if k & 1 and node != -1:
                node = self.parents[i][node]
            
            k >>= 1
        
        return node