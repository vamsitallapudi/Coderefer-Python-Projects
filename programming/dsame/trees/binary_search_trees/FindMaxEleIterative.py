from dsame.trees.common.BinarySearchTreeNode import *


def find_max_ele_iter(root: BinarySearchTreeNode):
    if not root:
        return root
    while root.right:
        root = root.right
    return root


print(find_max_ele_iter(initialize_BST()).data)
