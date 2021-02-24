class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        c = head
        num_nodes = 0
        while c is not None:
            num_nodes+=1
            c = c.next
        
        iters = num_nodes//k
        i = 0
        current, main_head, prev_group_end, current_group_end = head, None, None, None
        while i < iters:
            j = 0
            prev = None
            while j < k:
                if j == 0:
                    current_group_end = current
                Next = current.next
                current.next = prev
                prev = current
                current = Next
                j+=1
            if i == 0:
                main_head = prev
                prev_group_end = current_group_end
            else:
                prev_group_end.next = prev
                prev_group_end = current_group_end
            i+=1
        
        if current is not None:
            current_group_end.next = current
        
        return main_head