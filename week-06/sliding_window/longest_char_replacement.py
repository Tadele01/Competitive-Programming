class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        left, right = 0, 0
        counter, max_length, max_count = defaultdict(int), 0, 0
        
        for right in range(len(s)):
            counter[s[right]] +=1
            max_count = max(counter.values())
            while right - left + 1 - max_count > k:
                counter[s[left]] -= 1
                left += 1
                max_count = max(counter.values())
            max_length = max(max_length, right - left + 1)
        
        return max_length