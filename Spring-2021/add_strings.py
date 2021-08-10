class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        s1, s2 = [int(x) for x in num1], [int(x) for x in num2]
        carry, result = 0, []
        while s1 or s2:
            t1, t2 = s1.pop() if s1 else 0, s2.pop() if s2 else 0
            cur_sum = t1 + t2 + carry
            if cur_sum >= 10:
                mod = cur_sum % 10 if cur_sum > 10 else 0
                result.append(str(mod))
                carry = 1
            else:
                result.append(str(cur_sum))
                carry = 0
        if carry:
            result.append(str(carry))
        return ''.join(list(reversed(result)))