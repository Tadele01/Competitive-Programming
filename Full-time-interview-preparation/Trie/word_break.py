from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        return self.dfs(s, set(wordDict), 0, {})
    
    def dfs(self, word, words, i, cache):
        if i in cache:
            return cache[i]
        
        ans = False
        for j in range(i, len(word)):
            if word[i:j+1] in words:
                if j == len(word)-1 or self.dfs(word, words, j+1, cache):
                    ans = True

        cache[i] = ans
        
        return ans