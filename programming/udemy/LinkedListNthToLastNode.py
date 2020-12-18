# write a program to print a linked list's nth node to last node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nth_to_last_node(head, n):
    if not head:
        return None
    count = 0
    while head:
        if count == n:
            return head
        count += 1
        head = head.next
    return None


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    head = nth_to_last_node(a,3)

    while head:
        print(head.data)
        head = head.next

