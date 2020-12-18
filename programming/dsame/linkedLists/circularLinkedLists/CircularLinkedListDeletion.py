from dsame.linkedLists.circularLinkedLists.Common import print_and_iterate


class CLLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CLL:
    def __init__(self, head=None):
        self.head = head

    def delete_at_end(self, head):
        if not head or head.next is head:
            return None

        previous, current = head, head.next
        while current.next != head:
            previous = previous.next
            current = current.next
        previous.next = head
        return head

    def delete_at_start(self, head):
        if not head or head.next is head:
            return None

        current = head
        while current.next != head:
            current = current.next
        head = head.next
        current.next = head
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


if __name__ == "__main__":
    cll = CLL()
    cll.head = cll.insert_at_start(cll.head, 3)
    cll.head = cll.insert_at_start(cll.head, 2)
    cll.head = cll.insert_at_start(cll.head, 1)
    cll.head = cll.delete_at_start(cll.head)
    cll.head = cll.delete_at_end(cll.head)

    curr = cll.head
    curr = print_and_iterate(curr)
    while curr != cll.head:
        curr = print_and_iterate(curr)
