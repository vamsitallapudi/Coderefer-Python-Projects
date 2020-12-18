from dsame.trees.BinaryTreeNode import *


def no_of_leaves_iteration(root: BinaryTreeNode):
    count = 0
    queue = [root]
    while len(queue):
        temp = queue.pop(0)
        if not temp.left and not temp.right:
            count += 1
        else:
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    return count


print(no_of_leaves_iteration(initializeBinaryTree()))
