from leetcode.binaryTrees.TreeNode import *


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        o_stack, c_stack = [], []
        o_node, c_node = original, cloned
        while o_stack or o_node:
            while o_node:
                o_stack.append(o_node)
                c_stack.append(c_node)

                o_node = o_node.left
                c_node = c_node.left

            o_node = o_stack.pop()
            c_node = c_stack.pop()

            if o_node is target:
                return c_node

            o_node = o_node.right
            c_node = c_node.right

