# Definition for a binary tree node.
from typing import List
from leetcode.binaryTrees.TreeNode import *


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # to return an empty array if root is empty
        if not root:
            return []
        # appending the root value in array and recursively going into left and right subtrees
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


print(Solution().preorderTraversal(initializeBinaryTree()))
