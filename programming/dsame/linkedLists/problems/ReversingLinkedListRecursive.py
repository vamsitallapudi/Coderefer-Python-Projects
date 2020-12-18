from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def recursive_reverse(first):
    # if no elements in head
    if not first:
        return None
    if not first.next:
        return first
    # taking two elements every time, first and second
    second_ele = first.next
    # pointing first element to Null
    first.next = None
    # place where recursion happens if next elements are there
    reversed_part = recursive_reverse(second_ele)
    # pointing second element's next to first
    second_ele.next = first
    # returning the chain of reversed part
    return reversed_part


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    head = recursive_reverse(head)
    bll.print_data(head)
