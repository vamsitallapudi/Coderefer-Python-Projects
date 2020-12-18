# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.longestPath = 0
        self.depth(root)
        return self.longestPath

    def depth(self, node:TreeNode)-> int:
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.longestPath = max(self.longestPath, left + right)
        return max(left,right)+1


