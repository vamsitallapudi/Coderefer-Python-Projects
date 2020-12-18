from dsame.trees.BinaryTreeNode import *


def height_of_bin_tree_iterative(root: BinaryTreeNode):
    if not root:
        return 0

    queue = [root, None]
    level = 1
    while len(queue):
        temp = queue.pop(0)

        if not temp:
            if len(queue):
                queue.append(None)
                level += 1

        else:
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    return level


print(height_of_bin_tree_iterative(initializeBinaryTree()))
