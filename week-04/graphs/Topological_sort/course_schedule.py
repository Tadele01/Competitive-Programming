from collections import defaultdict
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        adj_list = defaultdict(list)
        for prerequire in prerequisites:
            adj_list[prerequire[1]].append(prerequire[0])
        for i in range(numCourses):
            indegree[i] = 0
        for prerequire in prerequisites:
            indegree[prerequire[0]] +=1
        queue = deque()
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        top_sort = deque()
        while queue:
            cur = queue.popleft()
            top_sort.append(cur)
            for neighbour in adj_list[cur]:
                indegree[neighbour] -=1
                if (indegree[neighbour])== 0:
                    queue.append(neighbour)
        if len(top_sort) == numCourses:
            return True
        return False
        
        