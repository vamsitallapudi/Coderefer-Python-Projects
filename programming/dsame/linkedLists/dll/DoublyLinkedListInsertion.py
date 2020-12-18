class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.data = data
        self.prev = prev
        self.next = next


def insert_at_start(head, data):
    # creating a new node and put data in it
    new_node = Node(data=data)
    # making new node's next reference to same node as head
    # and new node's prev to Null.(by default its null)
    new_node.next = head
    # changing head's prev to point to new_node
    if head:
        head.prev = new_node
    # now changing head to point to new node
    head = new_node
    return head


def insert_at_end(head, data):
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


def insert_at_pos(head, position, data):
    # if position is 0, we will be using our previous method
    if position is 0:
        return insert_at_start(head, data=data)

    # creating a new node and put data in it
    new_node = Node(data=data)
    pos = 0
    prev_node = head
    # traversing till position before is reached
    while pos < position - 1:
        pos += 1
        prev_node = prev_node.next
    # copy pointer of prev node's next to new node's next
    new_node.next = prev_node.next
    # point position/prev node's next node to new node
    prev_node.next = new_node
    # point new node's prev to prev_node
    new_node.prev = prev_node
    # point current node's prev node to new node
    if prev_node.next:
        prev_node.next.prev = new_node
    return head


if __name__ == '__main__':
    head = None
    head = insert_at_start(head, 1)
    head = insert_at_start(head, 2)
    head = insert_at_start(head, 3)
    head = insert_at_start(head, 4)
    head = insert_at_end(head, 5)
    head = insert_at_pos(head, 2, 10)

    while head:
        print(head.data, end=" ")
        head = head.next
