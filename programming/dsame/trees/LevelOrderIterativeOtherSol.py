from dsame.trees.BinaryTreeNode import *


# level order traversal reverse solution given by dsame

def level_order_traversal_rev_other(root: BinaryTreeNode):
    if not root:
        return

    queue, stack = [root], []

    while len(queue):
        temp = queue.pop(0)

        if temp.right:
            queue.append(temp.right)

        if temp.left:
            queue.append(temp.left)

        stack.append(temp)

    while len(stack):
        print(stack.pop().data)


level_order_traversal_rev_other(initializeBinaryTree())
