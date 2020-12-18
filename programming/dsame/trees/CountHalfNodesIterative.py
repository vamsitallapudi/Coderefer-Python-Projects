from dsame.trees.BinaryTreeNode import *


def count_half_nodes_iterative(root: BinaryTreeNode):
    if not root:
        return 0
    count = 0
    queue = [root]
    while len(queue):
        temp = queue.pop(0)
        if temp.left and temp.right:
            continue
        if temp.left:
            queue.append(temp.left)
            count += 1
        if temp.right:
            queue.append(temp.right)
            count += 1

    return count


print(count_half_nodes_iterative(initializeBinaryTreeWithTwoLevelsWithHalfNodes()))
