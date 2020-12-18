class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def initializeBinaryTree() -> TreeNode:
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(1, a, b)
    return c
