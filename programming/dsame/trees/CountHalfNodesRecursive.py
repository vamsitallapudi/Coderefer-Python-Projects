from dsame.trees.BinaryTreeNode import *


def count_half_nodes_recursive(root: BinaryTreeNode):
    if root.left and not root.right:
        return count_half_nodes_recursive(root.left) + 1
    if root.right and not root.left:
        return count_half_nodes_recursive(root.right) + 1

    return 0


print(count_half_nodes_recursive(initializeBinaryTreeWithTwoLevelsWithHalfNodes()))
