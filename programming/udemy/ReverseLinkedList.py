class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


def reverse(head):
    if not head:
        return None
    prev, curr = None, head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev


if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c

    head = reverse(a)

    while head:
        print(head.data)
        head = head.next
