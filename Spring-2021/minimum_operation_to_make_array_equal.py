from math import ceil, floor
class Solution:
    def minOperations(self, n: int) -> int:
        n = n - 2 
        return (ceil(n/2) + 1) * (floor(n/2)+1)