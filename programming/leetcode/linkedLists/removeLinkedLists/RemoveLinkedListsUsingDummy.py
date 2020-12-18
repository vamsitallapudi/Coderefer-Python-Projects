# Remove all elements from a linked list of integers that have value val.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    head = Solution().removeElements(a, 2)

    while head:
        print(head.val)
        head = head.next
