from dsame.trees.BinaryTreeNode import *


def level_order_reverse(root: BinaryTreeNode):
    if not root:
        return
    stack = [root]
    while len(stack):
        temp = stack[len(stack)-1]
        if not temp.left and not temp.right:
            break
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)

    while len(stack):
        print(stack.pop().data)


level_order_reverse(initializeBinaryTree())
