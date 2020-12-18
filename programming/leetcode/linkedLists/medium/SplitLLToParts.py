# Definition for singly-linked list.
from typing import List

from leetcode.linkedLists.medium.LinkedListComponents import initializeLinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def splitListToParts(self, root, k):
        # Count the length of the linked list
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        # Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            # skipping these many number of items to get ready for next split
            for i in range(num):
                prev, curr = curr, curr.next
        return res


#  find the length to split

def initializeLinkedListWith11():
    a = ListNode(0)
    b = ListNode(1)
    c = ListNode(2)
    d = ListNode(3)
    e = ListNode(4)
    # f = ListNode(5)
    # g = ListNode(6)
    # h = ListNode(7)
    # i = ListNode(8)
    # j = ListNode(9)
    # k = ListNode(10)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    # e.next = f
    # f.next = g
    # g.next = h
    # h.next = i
    # i.next = j
    # j.next = k

    return a


if __name__ == "__main__":
    a = initializeLinkedListWith11()
    Solution().splitListToParts(a, 3)
