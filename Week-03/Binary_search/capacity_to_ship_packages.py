from typing import List
class Solution:
    def get_day_count(self, weights, cur_weight):
        count = 0
        cur_sum= 0
        for value in weights:
            cur_sum += value
            if value > cur_weight:
                return float('inf')
            if cur_sum > cur_weight:
                count +=1
                cur_sum = value
        return count + 1
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        print(self.get_day_count(weights, 15))
        left, right = 1, sum(weights)
        ans = None
        while left <= right:
            mid = left + (right-left) // 2
            day_count = self.get_day_count(weights, mid)
            if day_count <= D:
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans