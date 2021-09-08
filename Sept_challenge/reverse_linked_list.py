from typing import Optional
from dataclasses import dataclass
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
@dataclass
class Container:
    prev_node: ListNode
    new_head: ListNode
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.dfs(head).new_head
    
    def dfs(self, node):
        if not node or not node.next:
            return Container(node, node)
        
        res = self.dfs(node.next)
        res.prev_node.next = node
        node.next = None
        res.prev_node = node
        return res