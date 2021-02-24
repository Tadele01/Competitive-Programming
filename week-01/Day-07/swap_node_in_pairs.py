class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            if prev:
                prev.val, curr.val = curr.val, prev.val
                prev = None
            else:
                prev = curr
            curr = curr.next
        return head