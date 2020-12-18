from dsame.trees.BinaryTreeNode import BinaryTreeNode, initializeBinaryTree


def preOrderNonRecursive(root: BinaryTreeNode):
    stack = []
    while True:
        while root:
            print(root.data)
            stack.append(root)
            #         if left subtree exists, move to it to add it to stack too.
            root = root.left

        if len(stack) <= 0:
            break
        #  coming back to node since it is pre order
        root = stack.pop()
        # now processing right side of the node
        root = root.right


print(preOrderNonRecursive(initializeBinaryTree()))
