class Solution:
    def is_bad_version(self, n:int)->bool:
        pass
    def first_bad_version(self, n:int)->bool:
        start = 1
        index = None
        while start <= n:
            middle (n + start) // 2
            if self.is_bad_version(middle):
                index = middle
                n = middle - 1
            else:
                start = middle + 1
            if (n-start) < 2:
                if self.is_bad_version(start):
                    return start
                elif self.is_bad_version(n):
                    return n
        return index
