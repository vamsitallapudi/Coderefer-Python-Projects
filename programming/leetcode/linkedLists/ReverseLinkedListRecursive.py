# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = self.reverseList(head.next)
        head.next.next = head  # main part - refer to notes
        head.next = None
        return p


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

    head = Solution().reverseList(a)

    while head:
        print(head.val)
        head = head.next
