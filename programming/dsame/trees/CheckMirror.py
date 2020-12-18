from dsame.trees.BinaryTreeNode import *


def check_mirror(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    else:
        return check_mirror(root1.left, root2.right) and check_mirror(root1.right, root2.left)


print(check_mirror(initializeBinaryTree(), initializeBinaryTreeMirror()))
