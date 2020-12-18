from dsame.trees.BinaryTreeNode import *


def search_element(ele, root: BinaryTreeNode):
    if not root:
        return False

    if ele == root.data:
        return True

    if search_element(ele, root.left):
        return True
    else:
        return search_element(ele, root.right)


print(search_element(4, initializeBinaryTree()))
