# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
#         find the mid node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
#         reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
#         compare first and second half of nodes
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True





