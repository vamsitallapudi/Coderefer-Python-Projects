# Given a linked list, remove the n-th node from the end of list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        # maintaining dummy to resolve edge cases
        dummy = ListNode(0)
        dummy.next = head
        # this is a two pointer technique.
        # Here we will be advancing one of the pointer to the n number of nodes and then advancing them equally
        prevPtr, nextPtr = dummy, dummy

        for i in range(n+1):
            nextPtr = nextPtr.next

        while nextPtr:
            prevPtr = prevPtr.next
            nextPtr = nextPtr.next

        prevPtr.next = prevPtr.next.next
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

