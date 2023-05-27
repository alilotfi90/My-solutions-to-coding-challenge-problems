# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))


def validateBstHelper(tree, min_value, max_value):
    if tree is None:
        return True

    if tree.value < min_value or tree.value >= max_value:
        return False

    # all elements in the left subtree is not in the range then return false
    return (validateBstHelper(tree.left, min_value, tree.value) and validateBstHelper(tree.right, tree.value ,max_value))
