# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowptr = head
        fastptr = head
        while(fastptr and fastptr.next):
            fastptr = fastptr.next.next
            slowptr = slowptr.next
        return slowptr.val
            
print(Solution().middleNode(ListNode([1,2,3,4,5,6])))

