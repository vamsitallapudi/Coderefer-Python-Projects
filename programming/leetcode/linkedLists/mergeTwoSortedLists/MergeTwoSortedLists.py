# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return l1
        if not l1:
            return l2
        if not l2:
            return l1
        head = temp = ListNode()
        while l1 or l2:
            if not l1:
                head.next = l2
                break
            elif not l2:
                head.next = l1
                break
            else:
                if l1.val <= l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
            head = head.next
        return temp.next


if __name__ == "__main__":
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
