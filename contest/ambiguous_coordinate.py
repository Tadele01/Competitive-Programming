class Solution(object):
    def ambiguousCoordinates(self, S):
        def pair_combination(left, right):
            res = []
            coordinates = [left, right]
            result = [[]]
            for coordinate in coordinates:
                result = [x+[y] for x in result for y in coordinate]
            for prod in result:
                res.append(tuple(prod))
            return res
                
        S = S.replace('(', '')
        S = S.replace(')', '')
        result = []
        cur_ans = []
        for i in range(1, len(S)):
            self.find_coordinates(S[:i], cur_ans)
            left, cur_ans = cur_ans, []
            self.find_coordinates(S[i:], cur_ans)
            right, cur_ans = cur_ans, []
            pairs = pair_combination(left, right)
            for pair in pairs:
                result.append("({}, {})".format(*pair))
        return result
    
    def find_coordinates(self, sub_string, cur_ans):
        length = len(sub_string)
        for i in range(1, length+1):
            left = sub_string[:i]
            right = sub_string[i:]
            if ((not left.startswith('0') or left == '0')
                    and (not right.endswith('0'))):
                if i != length:
                    cur_ans.append(left+'.'+right)
                else:
                    cur_ans.append(left+right)
                