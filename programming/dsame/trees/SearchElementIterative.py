from dsame.trees.BinaryTreeNode import *


def search_ele_iterative(ele, root: BinaryTreeNode):
    if not root:
        return False
    stack = [root]

    while len(stack) > 0:
        temp = stack.pop()
        if temp.data == ele:
            return True
        if temp.left:
            stack.append(temp.left)
        if temp.right:
            stack.append(temp.right)

    return False


print(search_ele_iterative(4, initializeBinaryTree()))
