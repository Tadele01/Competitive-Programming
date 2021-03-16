class Solution:
    def get_ascii(self, s_list):
        new_arr = []
        for value in s_list:
            new_arr.append(ord(value))
        return new_arr
    def get_result(self, arr):
        result = []
        for value in arr:
            if value > 122:
                diff = value - 123
                res = ord('a') + (diff % 26)
                result.append(chr(res))
            else:
                result.append(chr(value))
        return ''.join(result)
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        s_list = list(S)
        s_list_ascii = self.get_ascii(s_list)
        shifts_sum = sum(shifts)
        for i in range(len(s_list_ascii)):
            s_list_ascii[i] += shifts_sum
            shifts_sum -= shifts[i]
        result = self.get_result(s_list_ascii)
        return result
        