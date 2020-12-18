from dsame.trees.BinaryTreeNode import *


def count_full_nodes_recursive(root: BinaryTreeNode):
    if root.left:
        return count_full_nodes_recursive(root.left) + 1
    if root.right:
        return count_full_nodes_recursive(root.right) + 1
    if root.left and root.right:
        return 1
    return 0


print(count_full_nodes_recursive(initializeBinaryTreeWithTwoLevels()))
