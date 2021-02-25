from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses = set([i for i in range(numCourses)])
        if not prerequisites:
            return list(courses)
        adj_list, result, indegree = defaultdict(list), list(), defaultdict(int)
        for edge in prerequisites:
            adj_list[edge[1]].append(edge[0])
            if edge[1] in adj_list[edge[0]]:
                return []
            indegree[edge[0]] +=1
        queue = deque()
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
                result.append(i)
        while queue:
            cur_course = queue.popleft()
            for neighbour in adj_list[cur_course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] ==0:
                    indegree.pop(neighbour)
                    queue.append(neighbour)
                    if neighbour not in result:
                        result.append(neighbour)
                    courses.remove(neighbour)
        if indegree:
            return []
        if len(result) < numCourses:
            result.extend(list(courses))
            return result
        return result
                    
        
        
        