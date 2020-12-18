from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList

# reversing linked list iterative version

def reverse_linked_list(head):
    # iterative version
    temp, next = None, None
    while head:
        next = head.next
        head.next = temp
        temp = head
        head = next

    return temp


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    head = reverse_linked_list(head)
    bll.print_data(head)

