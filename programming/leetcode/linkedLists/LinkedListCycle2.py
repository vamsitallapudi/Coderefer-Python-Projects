# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                slowPtr = head
                while slowPtr and fastPtr:
                    if slowPtr == fastPtr:
                        return slowPtr
                    slowPtr = slowPtr.next
                    fastPtr = fastPtr.next
        else:
            return None

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    a.next = b
    b.next = a
    # c.next = d
    # d.next = b
    print(Solution().detectCycle(a).val)

