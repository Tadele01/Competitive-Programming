from collections import defaultdict
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj_list, visited, num_person= defaultdict(list), set(), len(quiet)
        result = [0] * num_person
        for edge in richer:
            adj_list[edge[1]].append(edge[0])
        for i in range(num_person):
            least_quiet = [float('inf'), None]        
            self.dfs(i, visited, adj_list, least_quiet, quiet)
            visited = set()
            if least_quiet[0] == float('inf'):
                result[i] = i
            else:
                if quiet[i] <= quiet[least_quiet[1]]:
                    result[i] = i
                else:
                    result[i] = least_quiet[1]
        return result
    
    def dfs(self, node, visited, adj_list, least_quiet, quiet):
        if node not in visited:h
            visited.add(node)
            for neighbour in adj_list[node]:
                if quiet[neighbour] < least_quiet[0]:
                    least_quiet[0] = quiet[neighbour]
                    least_quiet[1] = neighbour
                self.dfs(neighbour, visited, adj_list, least_quiet, quiet)

