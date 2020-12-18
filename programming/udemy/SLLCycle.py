class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None


def cycle_check(node):
    if not node:
        return False
    head = node
    node = node.nextnode
    while node:
        if node == head:
            return True
        node = node.nextnode
    return False


if __name__ == '__main__':
    # CREATE CYCLE LIST
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.nextnode = b
    b.nextnode = c
    c.nextnode = a  # Cycle Here!

    # CREATE NON CYCLE LIST
    x = Node(1)
    y = Node(2)
    z = Node(3)

    x.nextnode = y
    y.nextnode = z

    print(cycle_check(a))
