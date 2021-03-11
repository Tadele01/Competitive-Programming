class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right, max_length = 0, 0, 0
        while right < len(s):
            cost = abs(ord(s[right]) - ord(t[right]))
            if cost <= maxCost:
                maxCost -=cost
                right +=1
            else:
                max_length = max(max_length, right-left)
                while cost > maxCost:
                    first = abs(ord(s[left])-ord(t[left]))
                    maxCost += first
                    left +=1
        return max(max_length, right-left)