from dsame.trees.common.GenericBinaryTree import *


def siblings_count(root: GenericTreeNode):
    if not root or not root.nextSibling:
        return 0
    return 1 + siblings_count(root.nextSibling)


print(siblings_count(initializeGenericTreeForSiblings()))
