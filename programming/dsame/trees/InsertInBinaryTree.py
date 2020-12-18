from dsame.trees.BinaryTreeNode import *


# as it is a binary tree, we can insert wherever we want

def insertElement(ele, root: BinaryTreeNode):
    if not root:
        return root

    stack = [root]
    newNode = BinaryTreeNode(data=ele)

    while len(stack):
        temp = stack.pop()

        if temp.left:
            stack.append(temp.left)
        else:
            temp.left = newNode
            return root
        if temp.right:
            stack.append(temp.right)
        else:
            temp.right = newNode
            return root


printBinaryTree(insertElement(5, initializeBinaryTree()))
