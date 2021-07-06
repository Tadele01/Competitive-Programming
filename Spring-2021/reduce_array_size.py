from collections import Counter
from typing import List
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count_arr = sorted(Counter(arr).values(), reverse=True)
        n =  len(arr) / 2
        running_sum, count = 0, 0
        for freq in count_arr:
            if running_sum >= n:
                return count
            running_sum += freq
            count += 1
        
        return count