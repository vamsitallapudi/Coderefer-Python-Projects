# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child
# pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more
# children of their own, and so on, to produce a multilevel data structure


"""
# Definition for a Node.
# """


class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    # // Five situations:
    # // 1. null - no need to flatten, just return it
    # // 2. no child, no next - no need to flatten, it is the last element, just return it
    # // 3. no child, next - no need to flatten, go next
    # // 4. child, no next - flatten the child and done
    # // 5. child, next - flatten the child, connect it with the next, go next

    # // flattentail: flatten the node "head" and return the tail in its child (if exists)
    #     // the tail means the last node after flattening "head"

    def flatten(self, head: Node):
        # case 1: null
        if not head:
            return head
        self.flatten_tail(head)
        return head

    # return the tail of current branch
    def flatten_tail(self, head):
        if not head.child:
            if not head.next:
                # case 2
                return head
            # case 3 - no child, next -> go next
            return self.flatten_tail(head.next)
        else:
            nxt = head.next
            child = head.child
            head.child = None
            childTail = self.flatten_tail(child)
            head.next = child
            child.prev = head
            if nxt:
                # case 5
                childTail.next = nxt
                nxt.prev = childTail
                return self.flatten_tail(nxt)
            # CASE 4
            return childTail


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)
    a.next = b

    b.next = g
    b.prev = a
    b.child = c

    c.next = d

    d.next = e
    d.prev = c

    e.next = f
    e.prev = d

    x = Solution().flatten(a)

    while x:
        print(x.val)
        x = x.next
