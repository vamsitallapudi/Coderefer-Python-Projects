from dsame.trees.BinaryTreeNode import *


def sum_of_all_elements_iterative(root: BinaryTreeNode):
    if not root:
        return 0
    queue = [root]
    sum = 0
    while len(queue):
        temp = queue.pop(0)
        sum += temp.data
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)

    return sum


print(sum_of_all_elements_iterative(initializeBinaryTreeWithTwoLevels()))
