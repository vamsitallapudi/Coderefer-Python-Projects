from dsame.trees.common.GenericBinaryTree import *


def count_no_of_children(current: GenericTreeNode):
    # we just need to go to first child and count its siblings
    count = 0

    current = current.firstChild

    while current:
        count += 1
        current = current.nextSibling

    return count


print(count_no_of_children(initializeGenericTreeForSiblings()))
