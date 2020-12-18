from dsame.trees.common.BinarySearchTreeNode import *


def find_element_recursive(element, root: BinarySearchTreeNode) -> BinarySearchTreeNode:
    if not root:
        return root
    if element < root.data:
        return find_element_recursive(element, root.left)
    elif element > root.data:
        return find_element_recursive(element, root.right)
    return root


print(find_element_recursive(6, initialize_BST()))
