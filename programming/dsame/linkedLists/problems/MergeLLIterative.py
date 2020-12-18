# merge linked lists into a single list in sorted order iteratively
from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList, Node


def merge_lls_iterative(a, b):
    # creating a new node and referencing it.
    newNode = Node()
    # creating temp and referencing the created node. This will be iterating
    temp = newNode
    while a and b:
        if a.data <= b.data:
            temp.next = a
            temp = temp.next
            a = a.next
        else:
            temp.next = b
            temp = temp.next
            b = b.next

    if a:
        temp.next = a
    else:
        temp.next = b
    #     iterating the dummy temp to point to first node
    #     as new node is dummy one which we created for convenience.
    temp = newNode.next

    return temp


if __name__ == '__main__':
    bll1 = BaseLinkedList()
    bll2 = BaseLinkedList()
    head1 = bll1.initializebll(bll1)
    head2 = bll2.insert_at_end(bll2.head, 2)
    head2 = bll2.insert_at_end(head2, 8)
    head2 = bll2.insert_at_end(head2, 9)

    merged = merge_lls_iterative(head2, head1)
    while merged:
        print(merged.data)
        merged = merged.next
