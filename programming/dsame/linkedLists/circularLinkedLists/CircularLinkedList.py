from dsame.linkedLists.circularLinkedLists.Common import print_and_iterate


class CLLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def print_data(self):
        if self.head is None:
            return 0
        current = self.head
        while current.next != self.head:
            print(current.data, end=" ")
            current = current.next

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
    cll = CircularLinkedList()
    cll.head = cll.insert_at_start(cll.head, 3)
    cll.head = cll.insert_at_start(cll.head, 2)
    cll.head = cll.insert_at_start(cll.head, 1)

    curr = cll.head
    curr = print_and_iterate(curr)
    while curr != cll.head:
        curr = print_and_iterate(curr)

