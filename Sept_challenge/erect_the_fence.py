from typing import List
from math import atan2
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def cross(p1, p2, p3):
            return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

        start = min(points)
        points.pop(points.index(start))
        points.sort(key=lambda p: (atan2(p[1]-start[1], p[0]-start[0]), -p[1], p[0]))

        ans = [start]
        for p in points:
            ans.append(p)
            while len(ans) > 2 and cross(*ans[-3:]) < 0:
                ans.pop(-2)
        return ans