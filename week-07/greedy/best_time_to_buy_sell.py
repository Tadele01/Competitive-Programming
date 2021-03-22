class Solution:
    def max_profit(arr):
        max_profit = 0 
        for i in range(1, len(nums)):
            profit = nums[i] - nums[i-1]
            if profit > 0:
                max_profit +=1
        return max_profit
