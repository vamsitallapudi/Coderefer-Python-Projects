class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
"""
 Deleting a node at start. 
"""


def delete_at_start(head):
    # edge case: return if head is null
    if not head:
        return None
    head = head.next  # moving head to next node
    return head


"""
 Deleting a node at end. 
"""


def delete_at_end(head):
    # edge case
    if not head:
        return None

    prev_node = head
    # traversing until current node's next is null
    while prev_node.next.next:
        prev_node = prev_node.next
    # deleting the reference of previous node's next
    prev_node.next = None
    return head


def delete_at_pos(head, position):
    # edge case
    if not head:
        return None

    if position is 0:
        return head.next

    # maintaining previous and current nodes
    prev_node = head
    curr_node = head.next
    current_pos = 1
    while curr_node and current_pos < position:
        current_pos += 1
        prev_node = prev_node.next
        curr_node = curr_node.next
    prev_node.next = curr_node.next
    return head


def insert(head, data):
    if not head:
        return Node(data)
    temp = Node(data)
    temp.next = head
    head = temp
    return head


if __name__ == '__main__':

    # start with empty list
    head = None

    head = insert(head, 5)
    head = insert(head, 4)
    head = insert(head, 3)
    head = insert(head, 2)
    head = insert(head, 1)

    # delete at a given position
    head = delete_at_pos(head, 2)

    # deleting a node at start
    head = delete_at_start(head)

    # deleting a node at end
    head = delete_at_end(head)

    while head:
        print("{}".format(head.data), end=" ")
        head = head.next
