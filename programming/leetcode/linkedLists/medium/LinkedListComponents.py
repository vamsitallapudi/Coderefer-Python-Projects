# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, g: List[int]) -> int:
        count = 0

        while head:
            if head.val in g and (head.next is None or head.next.val not in g):
                count += 1
            head = head.next
        return count


def initializeLinkedList():
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    return a


if __name__ == "__main__":
    initializeLinkedList()
    print(Solution().numComponents(a, [0, 3, 1, 4]))
