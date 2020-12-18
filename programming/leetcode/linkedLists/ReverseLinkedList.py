# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # make prev node point to next node's next
        # make next node as head
        # dummy = ListNode(0)
        # dummy.next = head

        if not head or not head.next:
            return head

        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev







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

