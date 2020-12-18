# problem 28
from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def print_ll_from_end(head):
    if not head:
        return
    print_ll_from_end(head.next)
    print(head.data)


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    print_ll_from_end(head)
