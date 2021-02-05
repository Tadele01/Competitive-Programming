from heapq import heapify, heappop, heappushpop
class Solution:
    def heap_sort(self, arr:list)->list:
        sorted_ = []
        heapify(arr)
        while arr:
            sorted_.append(heappop(arr))
        return sorted_