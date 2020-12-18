class BinaryTreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


class Tree:

    def preOrder(self, root: BinaryTreeNode):
        if root:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)
