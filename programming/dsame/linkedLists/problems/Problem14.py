# similar to problem 11,
# but find length of the loop


def find_starting_node_of_loop(head):
    slowptr, fastptr = head, head
    count = 0
    is_a_loop = False
    while slowptr and fastptr and fastptr.next:
        if slowptr == fastptr:
            is_a_loop = True
            break
        slowptr = slowptr.next
        fastptr = fastptr.next.next

    if is_a_loop:
        # keep slow ptr as it is and move fast pointer till slow ptr is reached
        while slowptr != fastptr:
            count += 1
            fastptr = fastptr.next
        return count
    else:
        return 0  # no loop exists
