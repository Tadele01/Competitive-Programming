from math import ceil, floor
class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        n = n - 2 
        return (ceil(n/2) + 1) * (floor(n/2)+1)