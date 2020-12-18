from dsame.trees.common.BinarySearchTreeNode import *


def find_min_recursive(root: BinarySearchTreeNode):
    if not root:
        return root
    elif not root.left:
        return root
    else:
        return find_min_recursive(root.left)


print(find_min_recursive(initialize_BST()).data)
