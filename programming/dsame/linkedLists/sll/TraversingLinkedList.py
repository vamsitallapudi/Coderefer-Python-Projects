class Node:
    def __init__(self, data):
        self.data = data  # assigning the data passed
        self.next = None  # initializing the node as null


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


# actual code execution starts from here
if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.head = Node('a')
    second = Node('b')
    third = Node('c')
    linkedList.head.next = second
    second.next = third
    linkedList.traverse()
