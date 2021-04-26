class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        
        for word in words:
            same_match = False
            lookup = {}
            mapped = {}
            index = min(len(word), len(pattern))
            for i in range(index):
                if pattern[i] in lookup and lookup[pattern[i]] != word[i]:
                    same_match = True
                    break
                    
                if word[i] in mapped:
                    if mapped[word[i]] != pattern[i]:
                        same_match = True
                        break
                        
                lookup[pattern[i]] = word[i]
                mapped[word[i]] = pattern[i]
            if not same_match:
                result.append(word)
                
        return result
                    