from dsame.trees.common.BinarySearchTreeNode import *


def insert_ele_recursive(root: BinarySearchTreeNode, data: int):
    if not root:
        return BinarySearchTreeNode(data)
    else:
        if root.data == data:
            return root
        elif root.data > data:
            root.left = insert_ele_recursive(root.left, data)
        else:
            root.right = insert_ele_recursive(root.right, data)
    return root


print_inorder_BST(insert_ele_recursive(initialize_BST(), 10))
