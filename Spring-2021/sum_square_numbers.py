class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrs, i = set(), 0
        while i*i <= c:
            sqrs.add(i*i)
            i += 1
        
        for x in  sqrs:
            if c - x in sqrs:
                return True
        
        return False
                
        