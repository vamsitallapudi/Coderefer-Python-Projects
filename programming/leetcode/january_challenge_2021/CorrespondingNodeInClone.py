# recursive solution
from leetcode.binaryTrees.TreeNode import *


class Solution:
    answer = None

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.answer = c
                inorder(o.right, c.right)

        inorder(original, cloned)
        return self.answer
