class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # code to append / insert at end
    def insert_at_end(self, head, val):
        # creating a new node and put data in it
        new_node = ListNode(val)
        while not head:
            return new_node
        current = head
        while current and current.next:  # traversing till the last node
            current = current.next
        # change the next of last node
        current.next = new_node
        return head

    def initializebll(self, bll):
        for i in range(1, 7):
            self.head = bll.insert_at_end(self.head, i)
        return self.head

    def print_data(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next


def print_ll(head):
    while head:
        print(head.data, end=" ")
        head = head.next
