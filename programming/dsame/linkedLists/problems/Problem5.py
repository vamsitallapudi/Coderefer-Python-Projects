# find nth node of linked list from the last in single scan without using any other data type like hashmap etc.
from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def nth_node_from_end(head, n):
    p, temp = None, head
    for i in range(1, n):
        if temp:
            temp = temp.next
    while temp:
        if p:
            p = p.next
        else:
            p = head
        temp = temp.next

    if p:
        print(p.data)
    else:
        print(None)


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    nth_node_from_end(head, 5)