from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        length = len(cost)
        for i in range(2, len(cost)):
            min_before = min(cost[i-1], cost[i-2])
            cost[i] += min_before
        return min(cost[length-1], cost[length-2])