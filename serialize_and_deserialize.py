class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def serialize(root):
    res=[]
    def dfs(root,res):
        if not root:
            res.append('x')
            return
        res.append(root.val)
        dfs(root.left,res)
        dfs(root.right,res)
    dfs(root,res)
    return ' '.join(res)
def deserialize(s):
    def dfs(nodes):
        val=next(nodes)
        if not val or val=='x':
            return
        cur = Node(int(val))
        cur.left=dfs(nodes)
        cur.right=dfs(nodes)
        return cur
    return dfs(iter(s.split()))
def main():
    root=deserialize('6 4 3 x x 5 x x 8 x x')
    a=root.left
    print(a.val)
    b=a.left
    print(b.left)
    print(b.right)
if __name__ == "__main__":
  main()