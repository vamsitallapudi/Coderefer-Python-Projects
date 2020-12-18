from dsame.trees.BinaryTreeNode import *


def sum_of_all_elements_recursive(root: BinaryTreeNode):
    if not root:
        return 0

    return root.data + sum_of_all_elements_recursive(root.left) + sum_of_all_elements_recursive(root.right)


print(sum_of_all_elements_recursive(initializeBinaryTree()))
