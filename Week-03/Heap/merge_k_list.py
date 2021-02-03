from heapq import heappush, heappop, heapify
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists:list) -> ListNode:
        head=ListNode()
        heap=[]
        for i,node in enumerate(lists):
            if node:
                heappush(heap,(node.val,i))
        node=head
        while heap:
            cur_val,index=heappop(heap)
            node.next=ListNode(cur_val)
            node=node.next
            if lists[index]:
                lists[index]=lists[index].next
                if lists[index]:
                     heappush(heap,(lists[index].val,index))
        return head.next