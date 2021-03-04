from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        min_heap, result = [], []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum_ = nums1[i] + nums2[j]
                heappush(min_heap, (sum_, (nums1[i], nums2[j])))
        for i in range(k):
            if not min_heap:
                break
            data = heappop(min_heap)
            result.append(data[1])
        return result
        