from dsame.trees.BinaryTreeNode import *


def deepest_node(root: BinaryTreeNode):
    if not root:
        return

    queue = [root]
    temp = root
    while len(queue):
        temp = queue.pop(0)

        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
    return temp


print(deepest_node(initializeBinaryTree()).data)