from dsame.trees.common.BinarySearchTreeNode import *


def is_bst(root: BinarySearchTreeNode):
    if not root:
        return True
    if root.left and root.left.data > root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    if not is_bst(root.left) or not is_bst(root.right):
        return False
    return True


print(is_bst(create_BST_Two()))
