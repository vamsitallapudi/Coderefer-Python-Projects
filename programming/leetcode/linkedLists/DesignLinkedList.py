class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        if not self.head:
            return -1
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        x = Node(val=val)
        x.next = self.head
        self.head = x
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        x = Node(val=val)
        if not self.head:
            self.head = x
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = x

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index is 0:
            self.addAtHead(val)
        elif index is self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            x = Node(val=val)
            for i in range(index-1):
                curr = curr.next
            x.next = curr.next
            curr.next = x
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        curr = self.head
        if index is 0:
            self.head = curr.next
        else:
            for i in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1


if __name__ == "__main__":
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    print(linkedList.get(1))
    linkedList.deleteAtIndex(1)
    print(linkedList.get(1))

    # temp = linkedList.head
    # while temp:
    #     print(temp.val)
    #     temp = temp.next
