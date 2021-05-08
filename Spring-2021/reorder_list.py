# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: ListNode) -> None:
        deck, node = deque(), head
        while node != None:
            deck.append(node)
            node = node.next
            
        while len(deck) > 1:
            head, tail = deck.popleft(), deck.pop()
            tail.next = None
            if len(deck) > 0:
                tail.next = deck[0] 
                deck[0].next = None
            
            head.next = tail
        
        return head
