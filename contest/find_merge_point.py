def findMergeNode(head1, head2):
    head_1 = set()
    while head1:
        head_1.add(head1)
        head1 = head1.next
        
    while head2:
        if head2 in head_1:
            return head2.data
        head2 = head2.next