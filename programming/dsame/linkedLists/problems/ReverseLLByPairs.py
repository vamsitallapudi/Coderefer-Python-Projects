# problem 32 - Reversing linked list by pairs
from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def reverse_ll_pairs_recursive(head):
    if not head or not head.next:
        return
    temp = head.next
    head.next = temp.next
    temp.next = head
    head = temp
    head.next.next = reverse_ll_pairs_recursive(head.next.next)
    return head

if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    head = reverse_ll_pairs_recursive(head)
    while head:
        print(head.data)
        head = head.next