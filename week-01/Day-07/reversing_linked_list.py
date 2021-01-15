class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def reverseList(head):
    #reversing linked list using iteration

    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    if arr:
        head_val =arr.pop()
        node = ListNode(head_val)
        head = node
        while len(arr) != 0:
            cur = arr.pop()
            cur_node = ListNode(cur)
            node.next = cur_node
            node = cur_node
        return head

def reverseRecurssion(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self.reverseRecurssion(n, node)