from dsame.trees.common.BinarySearchTreeNode import *


# given a BST find LCA
def find_lca(root: BinarySearchTreeNode, a: BinarySearchTreeNode, b: BinarySearchTreeNode):
    while root:
        if (a.data < root.data < b.data) or (a.data > root.data > b.data):
            return root
        else:
            if root.data > a.data and root.data > b.data:
                root = root.left
            else:
                root = root.right
