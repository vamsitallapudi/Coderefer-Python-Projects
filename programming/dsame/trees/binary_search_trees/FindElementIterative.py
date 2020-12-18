from dsame.trees.common.BinarySearchTreeNode import *


def find_element_iterative(element, root: BinarySearchTreeNode):
    while root:
        if element == root.data:
            return root
        elif element < root.data:
            root = root.left
        else:
            root = root.right
    return None
