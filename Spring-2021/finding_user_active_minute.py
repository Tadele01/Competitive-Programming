from collections import Counter
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        UAM = defaultdict(set)
        for uid, minute in logs:
            UAM[uid].add(minute)
        
        for uid in UAM:
            UAM[uid] = len(UAM[uid])
        
        counter = Counter(UAM.values())
        
        result = [0] * k
        
        
        for key in counter:
            result[key-1] = counter[key]
        
        return result
        