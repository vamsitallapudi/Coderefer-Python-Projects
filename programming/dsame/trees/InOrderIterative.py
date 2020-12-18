from dsame.trees.BinaryTreeNode import BinaryTreeNode, initializeBinaryTree


def inOrderIterative(root: BinaryTreeNode):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left

        if len(stack) <= 0:
            break
        root = stack.pop()
        print(root.data)
        root = root.right


inOrderIterative(initializeBinaryTree())
