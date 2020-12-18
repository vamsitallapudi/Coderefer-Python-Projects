class BinaryTree(object):
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


def preOrder(tree: BinaryTree):
    if tree:
        print(tree.getRootVal())
        preOrder(tree.leftChild)
        preOrder(tree.rightChild)


def postOrder(tree: BinaryTree):
    if tree:
        preOrder(tree.leftChild)
        preOrder(tree.rightChild)
        print(tree.getRootVal())


def inOrder(tree: BinaryTree):
    if tree:
        preOrder(tree.leftChild)
        print(tree.getRootVal())
        preOrder(tree.rightChild)

