class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head:Node)->bool:
        if not head:
            return True
        return self.checker(head, tail=head)[0]
    
    def checker(self, head, tail):
        if not tail.next:
            return (tail.val == head.val, head)
        node_result = self.checker(head, tail.next)
        head = head.next
        return (node_result and head.val == tail.val, head)