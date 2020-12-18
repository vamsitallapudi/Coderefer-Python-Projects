# Write a program to find the node at which the intersection of two singly linked lists begins.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        #         finding length of both the lls
        nodeA, nodeB = headA, headB
        len1, len2 = 0, 0
        while nodeA:
            len1 += 1
            nodeA = nodeA.next

        while nodeB:
            len2 += 1
            nodeB = nodeB.next

        if len1 < len2:
            nodeA = headB
            nodeB = headA
            diff = len2 - len1
        else:
            nodeA = headA
            nodeB = headB
            diff = len1 - len2

        for i in range(diff):
            nodeA = nodeA.next

        while nodeA != nodeB:
            nodeA = nodeA.next
            nodeB = nodeB.next
        return nodeA


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(9)
    c = ListNode(1)
    d = ListNode(2)
    e = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    d.next = e

    f = ListNode(3)

    f.next = d

    print(Solution().getIntersectionNode(a, f).val)
