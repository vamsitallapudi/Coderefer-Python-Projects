from dsame.trees.BinaryTreeNode import *


def check_structurally_same(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if not root1 and not root2:
        return True

    if (not root1 and root2) or (not root2 and root1):
        return False

    return root1.data == root2.data and check_structurally_same(root1.left, root2.left) and check_structurally_same(
        root1.right, root2.right)


print(check_structurally_same(initializeBinaryTreeWithHalfNode(), initializeBinaryTreeWithHalfNode()))
