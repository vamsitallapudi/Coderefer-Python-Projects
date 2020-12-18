from dsame.trees.BinaryTreeNode import *


def mirror_of_a_tree(root: BinaryTreeNode):
    if not root:
        return
    if root.left:
        mirror_of_a_tree(root.left)
    if root.right:
        mirror_of_a_tree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp

    return root


printBinaryTree(initializeBinaryTreeWithTwoLevels())
x = mirror_of_a_tree(initializeBinaryTreeWithTwoLevels())
print()
printBinaryTree(x)
