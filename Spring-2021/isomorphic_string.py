class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_to_t = {}
        t_to_s = {}
        for x, y in zip(s, t):
            if x in s_to_t and s_to_t[x] != y or (y in t_to_s and t_to_s[y] != x):
                return False
            s_to_t[x] = y
            t_to_s[y] = x
        
        return True