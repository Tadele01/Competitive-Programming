def has_cycle(head):
    if head is None:
        return 0
    else:
        seen = []
        while head:
            if head in seen:
                return 1
            seen.append(head)
            head = head.next
        return 0