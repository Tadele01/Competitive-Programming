class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, visited = 0, 0, set()
        max_len = 0
        while right < len(s):
            if s[right] in visited:
                max_len = max(max_len, right-left)
                visited.remove(s[left])
                left +=1
            else:
                visited.add(s[right])
                right +=1
        return max(max_len, right-left)
            