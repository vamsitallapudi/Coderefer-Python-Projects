from dsame.trees.common.BinarySearchTreeNode import *


def find_max_ele_recursive(root: BinarySearchTreeNode):
    if not root:
        return root

    if not root.right:
        return root
    else:
        return find_max_ele_recursive(root.right)


print(find_max_ele_recursive(initialize_BST()).data)
