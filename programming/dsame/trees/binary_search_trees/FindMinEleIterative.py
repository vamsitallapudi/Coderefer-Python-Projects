from dsame.trees.common.BinarySearchTreeNode import *


def find_min_iterative(root: BinarySearchTreeNode):
    if not root:
        return None

    while root.left:
        root = root.left
    return root


print(find_min_iterative(initialize_BST()).data)
