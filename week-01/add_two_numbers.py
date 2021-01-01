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
def add_two_numbers(l1, l2):
    l1_int = []
    l2_int = []
    while l1 != None:
        l1_int.append(str(l1.val))
        l1 = l1.next
    while l2 != None:
        l2_int.append(str(l2.val))
        l2 = l2.next
    l1_str = int(''.join(l1_int))
    l2_str = int((''.join(l2_int)))
    summation = str(l1_str + l2_str)
    print(summation)
    n = ListNode(summation[-1])
    counter = 0
    if len(summation) == 1:
        return n
    for i in range(len(summation)-2, -1, -1):
        j = ListNode(summation[i])
        n.next = j
        counter +=1
        if counter == 1:
            z = n   
        n = j
    return z
    
