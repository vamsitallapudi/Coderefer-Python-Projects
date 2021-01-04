from common.ListNode import *


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        preHead = temp = ListNode(-1)  # dummy node
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        temp.next = l1 if l1 else l2

        return preHead.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)
d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
a.next = b
b.next = c

d.next = e
e.next = f

x = Solution().mergeTwoLists(a, d)

while x:
    print(x.val)
    x = x.next
