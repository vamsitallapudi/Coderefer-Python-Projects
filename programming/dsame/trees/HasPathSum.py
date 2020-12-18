from dsame.trees.BinaryTreeNode import *

# to check if there is a path with a given sum between root and tree

def has_path_sum(root: BinaryTreeNode, total):
    if not root:
        return total == 0
    else:
        total -= root.data
        return has_path_sum(root.left, total) or has_path_sum(root.right, total)


print(has_path_sum(initializeBinaryTree(), 2))
