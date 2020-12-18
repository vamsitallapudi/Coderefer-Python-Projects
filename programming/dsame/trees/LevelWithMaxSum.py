from dsame.trees.BinaryTreeNode import *


def level_with_max_sum(root: BinaryTreeNode):
    if not root:
        return 0
    queue = [root, None]
    level, maxLevel = 0, 0
    currSum, maxSum = 0, 0

    while len(queue):
        temp = queue.pop(0)

        if not temp:
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = level
            currSum = 0
            if len(queue):
                queue.append(None)
            level += 1

        else:
            currSum += temp.data
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

    return maxLevel


print(level_with_max_sum(initializeBinaryTreeWithTwoLevels()))
