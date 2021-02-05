from heapq import heappop, heapify, heappush
class MedianFinder:
    def __init__(self):
        self.small_elements = [] 
        self.large_elements = []  

    def addNum(self, num):
        if len(self.small_elements) == len(self.large_elements):
            heappush(self.large_elements, -heappushpop(self.small_elements, -num))
        else:
            heappush(self.small_elements, -heappushpop(self.large_elements, num))

    def findMedian(self):
        if len(self.small_elements) == len(self.large_elements):
            return float(self.large_elements[0] - self.small_elements[0]) / 2.0
        else:
            return float(self.large_elements[0])