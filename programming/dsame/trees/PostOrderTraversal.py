from dsame.trees.BinaryTreeNode import BinaryTreeNode, initializeBinaryTree


def post_order_traversal(root: BinaryTreeNode):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data)
