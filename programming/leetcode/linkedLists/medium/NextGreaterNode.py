# find next greater node and print it
# eg:
# Input: [2,1,5]
# Output: [5,5,0]

# Definition for singly-linked list.
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        position = -1
        stack, ans = [], []  # declaring empty lists

        while head:
            position += 1
            ans.append(0)
            # checking the top item of stack. Here -1 represents top most item
            # and 1 represent the tuple's second item, i.e. value
            while stack and stack[-1][1] < head.val:
                index, value = stack.pop()  # popping the top item of the stack
                ans[index] = head.val  # appending the value to our answer list

            stack.append((position, head.val))  # adding a tuple to the stack
            head = head.next
        return ans


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    x = Solution().nextLargerNodes(a)

    for i in x:
        print(i)
