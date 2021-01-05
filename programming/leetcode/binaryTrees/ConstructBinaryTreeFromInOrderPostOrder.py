from typing import List

from leetcode.binaryTrees.TreeNode import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        if len(inorder) != len(postorder):
            return None
        inorderMap = {}
        for i in range(0, len(inorder)):
            inorderMap[inorder[i]] = i

        return self.constructBinaryTree(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder)-1, inorderMap)

    def constructBinaryTree(self, inorder, inorderStart, inorderEnd, postorder, postorderStart, postorderEnd, dict):
        if inorderEnd < inorderStart or postorderEnd < postorderStart:
            return None
        node = TreeNode(postorder[postorderEnd])
        rootIndex = dict[postorder[postorderEnd]]
        leftchild = self.constructBinaryTree(
            inorder, inorderStart, rootIndex - 1, postorder, postorderStart,
                                   postorderStart + rootIndex - inorderStart - 1, dict)
        rightChild = self.constructBinaryTree(
            inorder, rootIndex + 1, inorderEnd, postorder,
                     postorderStart + rootIndex - inorderStart, postorderEnd - 1, dict)
        node.left = leftchild
        node.right = rightChild
        return node
