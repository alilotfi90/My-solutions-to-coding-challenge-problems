# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)

    while node.parent is not None:
        if node.parent.left == node:
            return node.parent
        node = node.parent

    return None


def getLeftMostChild(tree):
    while tree.left is not None:
        tree = tree.left
    return tree