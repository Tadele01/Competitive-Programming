from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_arr = Counter(answers)
        result = 0
        
        for num, freq in count_arr.items():
            if num == 0 :
                result += freq 
            elif num == 1:
                result += freq if freq % 2 == 0 else freq + 1
            elif num >= freq-1:
                result += 1 + num
            else:
                freq = freq -1 if freq % 2 == 0 else freq 
                div, mod = freq // (num + 1), freq % num 
                mod_sum = 1 + num if mod > 0 else 0
                result += (1 + num) * div + mod_sum
                
        return result
        
