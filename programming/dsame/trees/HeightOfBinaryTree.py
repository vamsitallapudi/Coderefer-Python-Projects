from dsame.trees.BinaryTreeNode import *


def height_of_binary_tree(root: BinaryTreeNode):
    if not root:
        return 0

    left = height_of_binary_tree(root.left)
    right = height_of_binary_tree(root.right)

    if left > right:
        return left + 1
    else:
        return right + 1


print(height_of_binary_tree(initializeBinaryTree()))
