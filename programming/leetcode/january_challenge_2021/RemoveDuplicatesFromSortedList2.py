# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from common.ListNode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = temp = ListNode(-1, head)  # since head might also contain duplicate value
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                temp.next = head.next
            else:
                temp = temp.next
            head = head.next

        return dummy.next
