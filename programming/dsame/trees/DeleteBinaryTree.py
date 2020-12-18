from dsame.trees.BinaryTreeNode import *


def delete_binary_tree(root: BinaryTreeNode):
    if not root:
        return

    delete_binary_tree(root.left)
    delete_binary_tree(root.right)
    return None


delete_binary_tree(initializeBinaryTree())
