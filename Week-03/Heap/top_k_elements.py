from heapq import heapify, heappop, heappush
class Solution:
    def topKFrequent(self, nums, k):
        hash_table = {}
        for elt in nums:
            if elt in hash_table:
                hash_table[elt] +=1
            else:
                hash_table[elt] = 1
        max_heap = []
        for elt, freq in hash_table.items():
            heappush(max_heap, (-1*freq, elt))
        result = []
        while k>0:
            result.append(heappop(max_heap)[1])
            k -= 1
        return result