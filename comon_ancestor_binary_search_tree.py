class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_on_bst(bst: Node, p: int, q: int) -> int:
    if bst.val==p or bst.val==q:
        return bst.val
    elif bst.val>p and bst.val<q:
        return bst.val
    elif bst.val<p and bst.val<q:
        return lca_on_bst(bst.right, p, q)
    else:
        return lca_on_bst(bst.left, p, q)