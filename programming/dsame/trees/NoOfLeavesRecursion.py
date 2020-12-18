from dsame.trees.BinaryTreeNode import *


def no_of_leaves(root: BinaryTreeNode):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return no_of_leaves(root.left) + no_of_leaves(root.right)


print(no_of_leaves(initializeBinaryTreeWithTwoLevels()))
