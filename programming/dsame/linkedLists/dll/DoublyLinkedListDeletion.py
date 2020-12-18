class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def delete_at_start(self, head):
        self.head = head.next
        self.head.left = None
        return self.head

    def delete_at_end(self, head):
        prev, current = head, head.next
        while current.next:
            prev = prev.next
            current = current.next
        prev.next = None
        return head

    def delete_at_pos(self, head, position):
        if position is 0:
            return self.delete_at_start(head)
        prev, current = head, head.next
        pos = 0
        while pos < position - 1 and current.next:
            pos += 1
            prev = prev.next
            current = current.next
        prev.next = prev.next.next
        return head

    # code to append / insert at end
    def insert_at_end(self, head, data):
        # creating a new node and put data in it
        new_node = Node(data=data)
        current = head

        # if Linked List is empty, make new node as head
        if not head:
            head = new_node
            return head

        # traversing till end
        while current.next:
            current = current.next
        # pointing the last node's next to new node
        current.next = new_node
        # pointing new node's previous
        new_node.prev = current
        return head


if __name__ == '__main__':
    head = None
    dll = DoublyLinkedList()
    head = dll.insert_at_end(head, 1)
    head = dll.insert_at_end(head, 2)
    head = dll.insert_at_end(head, 3)
    head = dll.insert_at_end(head, 4)
    head = dll.insert_at_end(head, 5)
    head = dll.insert_at_end(head, 6)

    head = dll.delete_at_start(head)
    head = dll.delete_at_end(head)
    head = dll.delete_at_pos(head, 5)

    while head:
        print(head.data, end=" ")
        head = head.next
