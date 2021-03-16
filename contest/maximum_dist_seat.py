from collections import deque
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        queue, max_dist, visited = deque(), 0, set()
        directions = [-1, 1]
        for i, value in enumerate(seats):
            if value == 1:
                queue.append((i,value, 0))
        while queue:
            cur_node, value, dist = queue.popleft()
            max_dist = max(max_dist, dist)
            for direction in directions:
                new_dir = direction + cur_node
                if self.is_valid(new_dir, visited, seats):
                    visited.add(new_dir)
                    if value == 1:
                        queue.append((new_dir, seats[new_dir],1))
                    else:
                        queue.append((new_dir, seats[new_dir], dist+1))
        return max_dist
    def is_valid(self, new_dir, visited, seats):
        if 0<= new_dir < len(seats) and seats[new_dir] != 1 and new_dir not in visited:
            return True
        return False