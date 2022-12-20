class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricaltwoTree(tree1,tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is not None and tree2 is None:
        return False
    if tree2 is not None and tree1 is None:
        return False
    return tree1.value==tree2.value and symmetricaltwoTree(tree1.left,tree2.right) and symmetricaltwoTree(tree1.right,tree2.left) 
    
def symmetricalTree(tree):
    return symmetricaltwoTree(tree.left,tree.right) 
