#given is non-empty linked list the numbers are in reverse order
#in the linked list each of the node contains a single digit
#after adding the two linked list return the sum as a linked list

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def size(self):
        counter = 1
        next_ = self.next
        while self.next != None:
            self.next = self.next.next
            counter +=1
        self.next = next_
        return counter
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l1_list = []
    l2_list = []
    while l1 != None:
        val = l1.val
        l1_list.append(str(val))
        l1 = l1.next
    while l2 != None:
        val = l2.val
        l2_list.append(str(val))
        l2 = l2.next
    l1_list.reverse()
    l2_list.reverse()
    l1_str = ''.join(l1_list)
    l2_str = ''.join(l2_list)
    summation = int(l1_str) + int(l2_str)
    summation_str = str(summation)
    if len(summation_str) == 1:
        return ListNode(int(summation_str[0]))
    summation_str = reversed(summation_str)
    head = next(summation_str)
    node = ListNode(int(head))
    data = True
    count = 0
    while data:
        data = next(summation_str, None)
        if data == None:
            break
        j = ListNode(int(data))
        node.next = j
        count +=1
        if count == 1:
            head = node
        node = j
    return head
    
