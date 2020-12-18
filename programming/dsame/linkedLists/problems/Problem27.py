def find_middle(head):
    ptr1, ptr2 = head, head  # ptr1 - fast ptr, ptr2 - slow ptr
    i = 0
    while head:
        if i == 0:
            ptr1 = ptr1.next
            i = 1

        else:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            i = 0

    return ptr2
