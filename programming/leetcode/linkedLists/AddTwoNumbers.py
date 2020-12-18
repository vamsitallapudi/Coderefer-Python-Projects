# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = temp = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            temp.next = ListNode(val)
            temp = temp.next
        return node.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(9)
    c = ListNode(4)
    d = ListNode(1)
    e = ListNode(8)
    a.next = b
    b.next = c

    d.next = e

    x = Solution().addTwoNumbers(a, d)

    while x:
        print(x.val)
        x = x.next
