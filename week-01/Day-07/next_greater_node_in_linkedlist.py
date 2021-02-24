class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        ret = [0 for b in range(len(arr))]
        stack = []
        for i in range(len(arr)):
            if len(stack) > 0:
                while len(stack) > 0 and arr[stack[-1]] < arr[i]:
                    ret[stack[-1]] = arr[i]
                    stack.pop()
            stack.append(i)
        return ret