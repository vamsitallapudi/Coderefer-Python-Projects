from dsame.trees.BinaryTreeNode import *


def size_of_bin_tree_iteration(root: BinaryTreeNode):
    if not root:
        return 0
    stack = [root]
    size = 0
    while len(stack):
        temp = stack.pop()
        size += 1
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)
    return size


print(size_of_bin_tree_iteration(initializeBinaryTree()))
