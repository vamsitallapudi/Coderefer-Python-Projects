from dsame.trees.BinaryTreeNode import *


def level_order(root: BinaryTreeNode):
    if not root:
        return

    queue = [root]  # initializing queue with root as input

    while len(queue) > 0:
        temp = queue.pop(0)  # popping first item since queue
        print(temp.data)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)


print(level_order(initializeBinaryTree()))
