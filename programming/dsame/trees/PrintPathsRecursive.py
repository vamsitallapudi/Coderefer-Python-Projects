from dsame.trees.BinaryTreeNode import *


def print_paths_recursive(root: BinaryTreeNode, path, path_len):
    if not root:
        return

    if len(path) > path_len:
        path[path_len] = root.data
    else:
        path.append(root.data)

    path_len += 1

    if not root.left and not root.right:
        printArray(path, path_len)
    else:
        print_paths_recursive(root.left, path, path_len)
        print_paths_recursive(root.right, path, path_len)


def printArray(path, path_len):
    for i in range(0, path_len):
        print(path[i])
    print()


print_paths_recursive(initializeBinaryTreeWithTwoLevels(), [], 0)
