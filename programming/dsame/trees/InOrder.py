from dsame.trees.BinaryTreeNode import BinaryTreeNode


def inOrder(root: BinaryTreeNode):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


a = BinaryTreeNode(2)
b = BinaryTreeNode(3)
c = BinaryTreeNode(1, a, b)

print(inOrder(c))
