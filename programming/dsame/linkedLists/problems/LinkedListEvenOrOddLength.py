from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def is_even_length(head):
    fastptr = head
    while fastptr and fastptr.next:
        fastptr = fastptr.next.next

    if not fastptr:
        return True
    else:
        return False


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    if is_even_length(head):
        print("Even")
    else:
        print("Odd")
