from dsame.trees.common.GenericBinaryTree import *


def sum(root: GenericTreeNode):
    if not root:
        return 0
    return root.data + sum(root.firstChild) + sum(root.nextSibling)


print(sum(initializeGenericTree()))
