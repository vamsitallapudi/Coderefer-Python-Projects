from dsame.trees.BinaryTreeNode import *


# using level order

def findMax(root: BinaryTreeNode) -> BinaryTreeNode:
    if not root:
        return root
    stack = [root]
    max = 0

    while len(stack):
        temp = stack.pop()
        if max < temp.data:
            # process
            max = temp.data
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)

    return max


print(findMax(initializeBinaryTree()))
