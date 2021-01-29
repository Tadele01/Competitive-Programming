class Solution:
    def binary_search(self, arr, target, low=0, index=0):
        low = 0
        high = len(arr) - 1
        mid = (low + high) // 2
        index += mid
        if arr:
            if arr[mid] == target:
                return index
            elif arr[mid] > target:
                index -= mid
                arr = arr[:mid] 
                return self.binary_search(arr, target, index=index)
            elif arr[mid] < target:
                arr = arr[mid+1:]
                index += 1
                return self.binary_search(arr, target, index=index)
        return -1


    def search(self, nums:list, target:int)->int:
        return self.binary_search(nums, target)