
class StackWithMin:

    def __init__(self):
        self.container = []
        self.min_collector = []

    def is_empty(self):
        return True if not self.container else False
    def push(self, data):
        self.container.append(data)
        if len(self.min_collector) == 0:
            self.min_collector.append(data)
            return
        if self.min_collector[-1] > data:
            self.min_collector.append(data)
        elif self.min_collector[-1] < data:
            self.min_collector.append(self.min_collector[-1])
        elif self.min_collector[-1] == data:
            self.min_collector.append(data)
        else:
            self.min_collector.append(data)
            self.container.append(data)
    def pop(self):
        if self.min_collector:
            self.min_collector.pop()
        if self.container:
            return self.container.pop()
        else:
            return 'Empty Stack'
    def peek(self):
        return self.container[-1]
    def min(self):
        #print(self.min_collector)
        if self.min_collector:
            return self.min_collector[-1]
        else:
            return 'Empty Stack'
    def size(self)->int:
        return len(self.container)
    def __repr__(self):
        stack = ''.join(str(self.container))
        return stack