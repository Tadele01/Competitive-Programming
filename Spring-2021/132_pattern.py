class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        i_th = nums[0]
        for j in range(1, len(nums)):
            if nums[j] > i_th:
                for k in range(j+1, len(nums)):
                    if nums[k] > i_th and nums[k] < nums[j]:
                        return True
            else:
                i_th = nums[j]
        
        return False