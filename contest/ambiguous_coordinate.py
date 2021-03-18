from itertools import product
class Solution(object):
    def ambiguousCoordinates(self, S):
        S = S.replace('(', '')
        S = S.replace(')', '')
        result = []
        for i in range(1, len(S)):
            left = self.find_coordinates(S[:i])
            right =  self.find_coordinates(S[i:])
            for pair in product(left, right):
                result.append("({}, {})".format(*pair))
        return result
    
    def find_coordinates(self, sub_string):
        length = len(sub_string)
        for i in range(1, length+1):
            left = sub_string[:i]
            right = sub_string[i:]
            if ((not left.startswith('0') or left == '0')
                    and (not right.endswith('0'))):
                yield left + ('.' if i != length else '') + right
                