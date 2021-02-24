class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_bra =  "({["
        close_bra = ")}])"
        dic = {"(": ")", "{":"}", "[":"]"}
		
        for i in range(len(s)):
            if s[i] in open_bra:
                stack.append(s[i])

            elif s[i] in close_bra:
                if len(stack) == 0:
                    return False
                item = stack.pop()
                if s[i] != dic[item]:
                    return False
        
        return len(stack) == 0