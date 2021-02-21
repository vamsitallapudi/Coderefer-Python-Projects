from common.ListNode import ListNode, LinkedList, print_ll


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0) -> ListNode:
        total_val = l1.val + l2.val + carry
        carry = total_val // 10
        node = ListNode(total_val % 10)
        if l1.next is not None or l2.next is not None or carry is not 0:
            if not l1.next:
                l1.next = ListNode(0)
            if not l2.next:
                l2.next = ListNode(0)

            node.next = self.addTwoNumbers(l1.next, l2.next, carry)

        return node


class Solution2:
    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if l1.next is not None or l2.next is not None or c != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret


bll = LinkedList()
bll2 = LinkedList()
head1 = bll.initializebll(bll)
head2 = bll2.initializebll(bll2, 2, 6)
print_ll(Solution().addTwoNumbers(head1, head2))
