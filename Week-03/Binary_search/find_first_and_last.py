class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_last = []
        left, right = 0, len(nums)- 1
        n = len(nums)
        self.binary_search(nums, first_last, n, left, right, target)
        first_last.sort()
        if first_last:
            value = [first_last[0], first_last[-1]]
        else:
            value = [-1, -1]
        return value
    def binary_search(self, nums, first_last, n, left, right, target):
        if(left <= right):
            mid = left + (right - left)//2
            if nums[mid] == target:
                first_last.append(mid)
                self.binary_search(nums, first_last, n, left, mid-1, target)
                self.binary_search(nums, first_last, n, mid+1, right, target)
            elif nums[mid] > target:
                self.binary_search(nums, first_last, n, left, mid-1, target)
            elif nums[mid] < target:
                self.binary_search(nums, first_last, n, mid+1, right, target)        
