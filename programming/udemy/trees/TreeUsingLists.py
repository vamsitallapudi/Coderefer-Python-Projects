def binaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


if __name__ == "__main__":
    r = binaryTree(3)
    insertLeft(r, 4)
    insertLeft(r, 5)
    insertLeft(r, 6)
    insertLeft(r, 7)
    insertRight(r, 8)
    print(r)
    print(getLeftChild(r))
    print(getRightChild(r))
    setRootVal(r, 9)
    print(r)
