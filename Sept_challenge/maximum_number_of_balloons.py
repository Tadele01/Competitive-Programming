from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def checker():
            for letter in word:
                if cnt_arr[letter] < 1:
                    return False
                cnt_arr[letter] -= 1
            return True        
        
        word, cnt_arr, ballons = 'balloon', Counter(text), 0
        
        while checker():
            ballons += 1
        
        return ballons