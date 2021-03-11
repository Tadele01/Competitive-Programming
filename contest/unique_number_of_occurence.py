from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = set(arr)
        unique_len = len(unique)
        counter = Counter(arr)
        freq = set(list(counter.values()))
        if len(freq) == unique_len:
            return True
        return False
        