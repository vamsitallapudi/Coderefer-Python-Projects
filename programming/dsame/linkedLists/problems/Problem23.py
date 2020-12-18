def find_intersecting_node(list1, list2):
    length1, length2, diff = 0, 0, 0
    head1 = list1, head2 = list2
    while head1:
        length1 += 1
        head1 = head1.next

    while head2:
        length2 += 1
        head2 = head2.next

    if length1 < length2:
        head1 = list2
        diff = length2 - length1
    else:
        head1 = list1
        diff = length1 - length2

    while diff > 0:
        head1 = head1.next
        diff -= 1

    while head1 and head2:
        if head1 == head2:
            return head1.data
        else:
            head1 = head1.next
            head2 = head2.next
    return None
