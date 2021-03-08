class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        c, b, a = nums.pop(), nums.pop(), nums.pop()
        while a+b <=c:
            if not nums:
                return 0
            a, b, c = nums.pop(), a, b
        return a+b+c