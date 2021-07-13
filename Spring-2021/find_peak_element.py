from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(-float('inf'))
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + ((right-left)//2)
            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid 
            elif nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid 
            elif nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid -1 
                
        return mid