from collections import defaultdict
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        weights = defaultdict(int)
        for i in range(len(order)):
            weights[order[i]] = i
        
        result = []
        for l in str:
            result.append((weights[l], l))
        
        result.sort(key=lambda x : x[0])
            
        return ''.join([x[1] for x in result])