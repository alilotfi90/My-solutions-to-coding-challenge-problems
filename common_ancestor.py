class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, node1, node2):
    def dfs(node,node1,node2):
        if node==None:
            return None
        if node==node1 or node==node2:
            return node
        a=dfs(node.left,node1,node2)
        b=dfs(node.right,node1,node2)
        if a==None:
            return b
        elif b==None:
            return a
        else:
            return node
    return dfs(root,node1,node2)
def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.right.right=Node(5)
    a=root.left.left
    b=root.right.right
    print(lca(root, a,b).val)
if __name__ == "__main__":
  main()