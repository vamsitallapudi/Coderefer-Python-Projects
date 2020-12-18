class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


# insertion of new node at front of linked list
def insert_at_front(head, data):
    # creating new node to be inserted
    new_node = Node(data)
    new_node.next = head  # pointing the new node's next to head
    head = new_node  # making the new node as head
    return head


def insert_at_end(head, data):
    new_node = Node(data)
    current = head
    while current.next:  # traversing till the last node
        current = current.next
    # change the next of last node
    current.next = new_node
    return head


def insert_at_pos(head, data, position):
    # edge case: check if pos is 0
    new_node = Node(data)
    if position is 0:
        new_node.next = head
        head = new_node
        return head

    pos = 0
    new_node = Node(data)
    curr_node = head
    # iterating till the position is reached
    while curr_node.next and pos < position - 1:
        pos += 1
        curr_node = curr_node.next
    # making new node's next as current node's next
    new_node.next = curr_node.next
    # making current node's next point to new node
    curr_node.next = new_node
    return head


if __name__ == '__main__':
    head = None

    head = insert_at_front(head, 1)
    head = insert_at_front(head, 2)
    head = insert_at_end(head, 3)
    head = insert_at_end(head, 4)
    head = insert_at_pos(head, 12, 1)

    while head:
        print('{}'.format(head.data), end=" ")
        head = head.next
