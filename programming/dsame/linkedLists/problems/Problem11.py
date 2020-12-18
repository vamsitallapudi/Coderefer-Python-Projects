"""
Check whether the given linked list is null terminated or not.
If it is, find the starting node of the loop.
"""


def find_starting_node_of_loop(head):
    slowptr, fastptr = head, head
    is_a_loop = False
    while slowptr and fastptr and fastptr.next:
        if slowptr == fastptr:
            is_a_loop = True
            break
        slowptr = slowptr.next
        fastptr = fastptr.next.next

    if is_a_loop:
        slowptr = head
        while slowptr and fastptr and slowptr != fastptr:
            slowptr = slowptr.next
            fastptr = fastptr.next
        return slowptr
    else:
        return None
