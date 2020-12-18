# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = self.populateStack(l1)
        stack2 = self.populateStack(l2)
        carry = 0

        head = ListNode()

        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
            carry, val = divmod(carry, 10)
            head.next, head.next.next = ListNode(val), head.next

        return head.next

    def populateStack(self, head):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return stack


if __name__ == "__main__":

    a = ListNode(1)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)

    a.next = b
    b.next = c

    d.next = e

    head = Solution().addTwoNumbers(a, d)

    while head:
        print(head.val)
        head = head.next
