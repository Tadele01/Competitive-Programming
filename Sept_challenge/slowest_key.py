from typing import List
from collections import defaultdict
class Solution:
    def slowestKey(self, leave: List[int], keys: str) -> str:
        time = defaultdict(int)
        time[keys[0]] = leave[0]
        for i in range(1, len(leave)):
            duration = leave[i] - leave[i-1]
            time[keys[i]] = max(time[keys[i]], duration)
        
        max_val = max(time.values())
        return max(key for key in time if time[key] == max_val)
        