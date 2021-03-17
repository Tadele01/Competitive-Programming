from typing import Listr
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for value in strs:
            sorted_val = str(sorted(value))
            result[sorted_val].append(value)
        return list(result.values())