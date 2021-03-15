class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for value in s:
            if not stack:
                stack.append((value, 1))
            else:
                top, freq = stack[-1]
                if top == value:
                    stack[-1] = (value, freq+1)
                    if freq+1 == k:
                        stack.pop()
                else:
                    stack.append((value, 1))
        stack = [i[0] * i[1] for i in stack]
        return ''.join(stack)