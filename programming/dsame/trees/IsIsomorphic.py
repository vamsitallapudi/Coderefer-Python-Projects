from dsame.trees.BinaryTreeNode import *


def is_isomorphic(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if not root1 and not root2:
        return True

    if (not root1 and root2) or (root1 and not root2):
        return False

    return is_isomorphic(root1.left, root2.left) and is_isomorphic(root1.right, root2.right)
