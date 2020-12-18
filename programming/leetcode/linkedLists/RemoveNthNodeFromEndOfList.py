# Given a linked list, remove the n-th node from the end of list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0)
        dummy.next = head
        # find length of node
        length = 0
        first = head
        while first:
            first = first.next
            length += 1

        length -= n
        x = dummy
        while length > 0:
            x = x.next
            length -= 1
        x.next = x.next.next
        return dummy.next


if __name__ == "__main__":

    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = Solution().removeNthFromEnd(a, 2)

    while head:
        print(head.val)
        head = head.next
