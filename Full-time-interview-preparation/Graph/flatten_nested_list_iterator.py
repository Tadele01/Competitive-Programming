from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque()
        for n in nestedList:
            ints = []
            self.flatten(n, ints)
            for i in ints:
                self.queue.append(i)
    def next(self) -> int: 
        if self.hasNext():
            return self.queue.popleft()
        
    
    def hasNext(self) -> bool:
        if self.queue:
            return True
        return False
    def flatten(self, n, ints):
        if n.isInteger():
            ints.append(n.getInteger())
            return 
        l = n.getList()
        for val in l:
            if val.isInteger():
                ints.append(val.getInteger())
            else:
                self.flatten(val, ints)