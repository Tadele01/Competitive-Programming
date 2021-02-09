class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        A, B = set(), set()
        for i in range(len(graph)):
            if i not in B and i not in A:
                result = self.helper(graph, i, A, B)
                if (result == False):
                    return False
        return True
    def helper(self, graph, current, A, B):
        for child in graph[current]:
            if child in A:
                return False
            if child not in B:
                B.add(child)
                if (self.helper(graph, child, B, A)) == False:
                    return False
        return True
                