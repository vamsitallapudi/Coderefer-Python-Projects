class GenericTreeNode:
    def __init__(self, data=None, firstChild=None, nextSibling=None):
        self.data = data
        self.firstChild = firstChild
        self.nextSibling = nextSibling


def initializeGenericTree() -> GenericTreeNode:
    c = GenericTreeNode(4)
    e = GenericTreeNode(5)
    a = GenericTreeNode(3, firstChild=c, nextSibling=e)
    b = GenericTreeNode(2, nextSibling=a)
    d = GenericTreeNode(1, firstChild=b)
    return d


def initializeGenericTreeForSiblings() -> GenericTreeNode:
    c = GenericTreeNode(4)
    d = GenericTreeNode(5)
    a = GenericTreeNode(3, firstChild=c, nextSibling=d)
    b = GenericTreeNode(2, firstChild=a)
    return b
