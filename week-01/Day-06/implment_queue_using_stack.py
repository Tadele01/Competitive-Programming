class MyStack(object):
    def __init__(self):
        self.collector = []
    def size(self):
        return len(self.collector)
    def pop(self):
        if self.collector:
            return self.collector.pop()
        else:
            return None
    def peek(self):
        if self.collector:
            return self.collector[-1]
        else:
            return None
    def push(self, data):
        self.collector.append(data)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = MyStack()
        self.stack2 = MyStack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.stack1.size() == 0:
            self.stack1.push(x)
        else:
            while self.stack1.size() !=0:
                top = self.stack1.pop()
                self.stack2.push(top)
            self.stack1.push(x)
            while self.stack2.size() != 0:
                top = self.stack2.pop()
                self.stack1.push(top)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack1.peek()
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if self.stack1.size() == 0 else False