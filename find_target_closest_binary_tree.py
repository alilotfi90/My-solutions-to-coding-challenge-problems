def findClosestValueInBst(tree, target):
    if tree==None:
        return None
    if tree.value==target:
        return target
    if tree.value>target:
        if tree.left!=None:
            if abs(findClosestValueInBst(tree.left, target)-target)<abs(tree.value-target):
                return findClosestValueInBst(tree.left, target)
            else:
                return tree.value
        else:
            return tree.value
    if tree.value<target:
        if tree.right!=None:
            if abs(findClosestValueInBst(tree.right, target)-target)<abs(tree.value-target):
                return findClosestValueInBst(tree.right, target)
            else:
                return tree.value
        else:
            return tree.value
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def main():
    print('findClosestValueInBst calculates closest to element to target in tree')
if __name__ == "__main__":
  main()