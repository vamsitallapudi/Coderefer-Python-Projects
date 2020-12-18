from dsame.trees.BinaryTreeNode import *


def count_full_nodes_iter(root: BinaryTreeNode):
    if not root:
        return 0

    queue = [root]
    count = 0
    while len(queue):
        temp = queue.pop(0)
        if temp.left and temp.right:
            count += 1
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    return count


print(count_full_nodes_iter(initializeBinaryTreeWithTwoLevels()))
