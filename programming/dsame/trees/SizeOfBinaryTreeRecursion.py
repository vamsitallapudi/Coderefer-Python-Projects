from dsame.trees.BinaryTreeNode import *


def size_of_bin_tree(root: BinaryTreeNode):
    if not root:
        return 0
    return size_of_bin_tree(root.left) + 1 + size_of_bin_tree(root.right)


print(size_of_bin_tree(initializeBinaryTree()))
