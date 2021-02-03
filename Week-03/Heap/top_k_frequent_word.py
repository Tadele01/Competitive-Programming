from heapq import heappop, heapify, heappush

class Solution:
    def topKFrequentWord(self, words:list, k:int)->list:
        hash_table = {}
        for word in words:
            if word in hash_table:
                hash_table[word] += 1
            else:
                hash_table[word] = 1
        
        max_heap = []
        for key, value in hash_table.items():
            heappush(max_heap, (-1*value, key))
        result = []
        for _ in range(k):
            result.append(heappop(max_heap)[1])
        return result
