from dsame.trees.common.BinarySearchTreeNode import *


def deleteNode(root: BinarySearchTreeNode, data: int):
    temp = None
    # base case
    if not root:
        print("No element is present in the tree")
        return root
    # if data which needs to be deleted is less than root's data,
    # then it lies in left subtree of the root.
    elif data < root.data:
        root.left = deleteNode(root.left, data)
    # if data which needs to be deleted is greater than root's data,
    # then it lies in right subtree of the root.
    elif data > root.data:
        root.right = deleteNode(root.right, data)
    # If the data is same as root's data, then this is the node to be deleted
    else:
        # found element
        if root.left and root.right:  # both children are present for that node
            # replace with largest from left subtree
            temp = find_max_ele(root.left)
            root.data = temp.data
            # delete the inorder predecessor
            root.left = deleteNode(root.left, temp.data)
        else:
            # one child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
    return root


def find_max_ele(root: BinarySearchTreeNode):
    if not root:
        return root
    while root.right:
        root = root.right
    return root


print_inorder_BST(deleteNode(create_BST(), 50))
