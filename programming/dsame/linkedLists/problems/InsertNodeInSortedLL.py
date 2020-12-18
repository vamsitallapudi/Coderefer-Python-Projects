def insert_node(head, node):
    if not head:
        return node
    current, temp = head, None
    while current and current.data < node.data:
        temp = current
        current = current.next
    # now current is bigger than the data in the node.
    node.next = current
    temp.next = node
    return head
