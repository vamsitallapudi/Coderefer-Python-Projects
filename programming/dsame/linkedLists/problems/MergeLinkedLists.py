# merge linked lists into a single list in sorted order
from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def merge_lls_recursive(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.data <= b.data:
        result = a
        result.next = merge_lls_recursive(a.next, b)
    else:
        result = b
        result.next = merge_lls_recursive(a, b.next)

    return result


if __name__ == '__main__':
    bll1 = BaseLinkedList()
    bll2 = BaseLinkedList()
    head1 = bll1.initializebll(bll1)
    head2 = bll2.insert_at_end(bll2.head, 2)
    head2 = bll2.insert_at_end(head2, 8)
    head2 = bll2.insert_at_end(head2, 9)

    merged = merge_lls_recursive(head2, head1)
    while merged:
        print(merged.data)
        merged = merged.next