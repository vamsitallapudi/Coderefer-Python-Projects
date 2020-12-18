def is_looped_linked_list(head) -> bool:
    """
    using slow pointer, fast pointer technique

    For each iteration,
    slow pointer -> moves 1 step ahead
    fast pointer -> moves 2 steps ahead
    :param head:
    :return:
    """
    slowptr, fastptr = head, head
    while slowptr and fastptr and fastptr.next:
        if slowptr == fastptr:
            return True
        slowptr = slowptr.next
        fastptr = fastptr.next.next

    return False
