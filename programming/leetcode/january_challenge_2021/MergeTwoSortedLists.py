from common.ListNode import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def insert(head, data):
    if not head:
        return ListNode(data)
    while head.next:
        head = head.next
    head.next = ListNode(data)
    return head


head1 = ListNode(1)
a = insert(head1, 2)
b = insert(a, 4)
head2 = ListNode(1)
c = insert(head2, 3)
d = insert(c, 4)

print(print_ll(Solution().mergeTwoLists(head1, head2)))
