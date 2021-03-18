class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        cur_node, prev_node = head, None
        count = 0
        while cur_node: 
            if prev_node and prev_node.val in G and cur_node.val in G:
                next_elt = cur_node.next
                G.remove(prev_node.val)
                G.remove(cur_node.val)
                self.remove_elt(next_elt, G)
                count +=1
            prev_node, cur_node = cur_node, cur_node.next
        return count + len(G)
    def remove_elt(self, node, G):
        if node and node.val in G:
            G.remove(node.val)
            self.remove_elt(node.next, G)