from collections import defaultdict
class Solution:
    def solve(self, left, right):
        incoming = defaultdict(int)
        n = len(left)
        for i in range(n):
            l_ptr, r_ptr = left[i], right[i]
            if l_ptr != -1:
                incoming[l_ptr] +=1
                if incoming[l_ptr] > 1:
                    return False
            if r_ptr != -1:
                incoming[r_ptr] +=1
                if incoming[r_ptr] > 1:
                    return False
            
        root = None
        for i in range(n):
            if incoming[i] == 0:
                root = i
                break
                
        if root == None:
            return False
        return True if self.count(root, left, right) == n else False
    
    def count(self, root, left, right):
        if root == -1:
            return 0
        
        return 1 + self.count(left[root], left, right) + self.count(right[root], left, right)