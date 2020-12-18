class BinarySearchTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def initialize_BST():
    a = BinarySearchTreeNode(6)
    b = BinarySearchTreeNode(8)
    return BinarySearchTreeNode(7, a, b)


def print_inorder_BST(root: BinarySearchTreeNode):
    if not root:
        return root
    if root.left:
        print_inorder_BST(root.left)
    print(root.data)
    if root.right:
        print_inorder_BST(root.right)


def insert(node: BinarySearchTreeNode, data):
    if not node:
        return BinarySearchTreeNode(data)
    if data < node.data:
        node.left = insert(node.left, data)
    elif data > node.data:
        node.right = insert(node.right, data)
    return node


def create_BST():
    """ creating the following BST
                  50
               /     \
              30      70
             /  \    /  \
           20   40  60   80 """
    root = BinarySearchTreeNode(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 60)
    root = insert(root, 80)
    root = insert(root, 70)
    return root


def create_BST_Two():
    """ creating the following BST
                  4
               /     \
              2       8
                     /  \
                    5   10
                     \
                      7
                    /
                   6
    """

    root = BinarySearchTreeNode(4)
    root = insert(root, 2)
    root = insert(root, 8)
    root = insert(root, 5)
    root = insert(root, 10)
    root = insert(root, 7)
    root = insert(root, 6)
    return root
