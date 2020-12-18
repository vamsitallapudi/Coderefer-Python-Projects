from dsame.trees.BinaryTreeNode import *


def maxEle(root: BinaryTreeNode) -> BinaryTreeNode:
    maximum = 0
    if root:
        root_val = root.data
        left = maxEle(root.left)
        right = maxEle(root.right)
        maximum = max(left, right, root_val)
    return maximum


print(maxEle(initializeBinaryTree()))
