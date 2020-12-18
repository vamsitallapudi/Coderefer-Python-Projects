# Definition for singly-linked list.

# 1. find the length of the ll
# 2. iterate till len - k
# 3. chop off and add len-k+1 to len node and add to start

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k is 0:
            return head
        len, temp = 0, head
        # step 1 - identifying length
        while temp:
            len += 1
            temp = temp.next

        # step - 2 - split the ll into two
        temp = head
        if k > len:
            k %= len
        if k == len:
            return head
        for i in range(len - k - 1):
            head = head.next

        # creating a dummy
        new_head = temp_1 = ListNode()
        temp_1.next = head.next
        head.next = None
        while temp_1.next:
            temp_1 = temp_1.next
        # step -3 attaching new head's end to old head
        temp_1.next = temp

        return new_head.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    # c = ListNode(2)
    # d = ListNode(4)
    # e = ListNode(5)
    a.next = b
    # b.next = c
    # c.next = d
    # d.next = e

    head = Solution().rotateRight(a, 2)

    while head:
        print(head.val)
        head = head.next
