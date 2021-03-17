from collections import deque
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque(['/'])
        last_seen = []
        path += '/'
        for i in range(1, len(path)):
            if not last_seen and path[i] == '/':
                continue
            elif path[i] == '/' and last_seen:
                res = ''.join(last_seen)
                if res == '..' and len(stack)>1:
                    stack.pop()
                elif res == '.':
                    last_seen = []
                    continue
                elif res != '..' and res != '.':
                    stack.append('/'+res)
                last_seen = []
            else:
                last_seen.append(path[i])
        
        if len(stack) > 1:
            stack.popleft()
        return ''.join(stack)