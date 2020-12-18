class CLLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, head):
        self.head = head

    def insert_at_end(self, head, data):
        new_node = CLLNode(data=data)
        # initialize new variable called current
        if not head:
            new_node.next = new_node
            head = new_node
            return head
        current = head
        while current.next != head:
            current = current.next

        new_node.next = head
        current.next = new_node
        return head

    def insert_at_start(self, head, data):
        new_node = CLLNode(data=data)
        # initialize new variable called current
        if not head:
            new_node.next = new_node
            head = new_node
            return head
        current = head
        while current.next != head:
            current = current.next

        new_node.next = head
        current.next = new_node
        head = new_node
        return head


def print_and_iterate():
    global current
    print("{}".format(current.data), end=" ")
    current = current.next


if __name__ == "__main__":
    head = None
    cll = CircularLinkedList(head)
    head = cll.insert_at_start(head, 3)
    head = cll.insert_at_start(head, 2)
    head = cll.insert_at_start(head, 1)
    head = cll.insert_at_end(head, 4)
    head = cll.insert_at_end(head, 5)

    current = head
    print_and_iterate()
    while current != head:
        print_and_iterate()
