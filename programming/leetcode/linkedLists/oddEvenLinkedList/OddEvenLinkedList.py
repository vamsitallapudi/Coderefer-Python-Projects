# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)

        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next

            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next


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

    head = Solution().oddEvenList(a)

    while head:
        print(head.val)
        head = head.next
