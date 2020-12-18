from dsame.trees.BinaryTreeNode import BinaryTreeNode, initializeBinaryTree


def post_order_iterative(root: BinaryTreeNode):
    stack = []
    prev = None
    while True:
        while root:
            stack.append(root)
            root = root.left

        while len(stack):
            root = stack[len(stack) - 1]
            if (not root.right) or (root.right == prev):
                print(root.data)
                stack.pop()
                prev = root
                root = None
            else:
                root = root.right
                break

        if len(stack) <= 0:
            break


print(post_order_iterative(initializeBinaryTree()))
