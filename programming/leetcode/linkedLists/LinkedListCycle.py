# given a linked list, determine if it has a cycle in it

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                return True
        return False


if __name__ == "__main__":
    x = ListNode(1)
    print(Solution().hasCycle(x))
