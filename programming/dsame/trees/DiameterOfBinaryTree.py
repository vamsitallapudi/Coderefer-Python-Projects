from dsame.trees.BinaryTreeNode import *

"""
diameter of a binary tree calculating nodes. To calculate edges only remove the addition of 
1 from line 14
"""


class Solution:
    def diameterOfBinaryTree(self, root: BinaryTreeNode) -> int:
        if not root:
            return 0
        lHeight = self.height(root.left)
        rHeight = self.height(root.right)
        lDiameter = self.diameterOfBinaryTree(root.left)
        rDiameter = self.diameterOfBinaryTree(root.right)
        return max(lHeight + rHeight, max(lDiameter, rDiameter)) + 1

    def height(self, root: BinaryTreeNode):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


print(Solution().diameterOfBinaryTree(initializeBinaryTreeWithTwoLevels()))
