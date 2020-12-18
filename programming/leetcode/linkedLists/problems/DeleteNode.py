class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_node(self, node: Node):
        node.val = node.next.val
        node.next = node.next.next

