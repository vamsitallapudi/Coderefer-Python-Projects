# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        while l1 and l2:

            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

        curr.next = l1 or l2
        return dummy.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)
    a.next = b
    b.next = c

    d.next = e
    e.next = f

    x = Solution().mergeTwoLists(a, d)
