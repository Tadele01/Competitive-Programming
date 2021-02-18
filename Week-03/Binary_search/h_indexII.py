from typing import List
class Solution:
    def h_indexII(self, citations:List)->int:
        left, right, N, h_index = 0, len(citations)-1, len(citations), 0
        while left <= right:
            mid = left + ((right - left)//2)
	    if citations[mid] >= (N-mid):
	        h_index = N-mid
	        right = mid - 1
	    else:
	        left = mid + 1
	return h_index        
