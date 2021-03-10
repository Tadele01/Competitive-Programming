class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push_pointer, stack = 0, []
        for i, value in enumerate(popped):
            if stack and stack[-1] == value:
                stack.pop()
                continue
            while push_pointer < len(pushed)-1:
                front = pushed[push_pointer]
                push_pointer +=1
                if front != value:
                    stack.append(front)
                else:
                    break
        return len(stack) == 0
                