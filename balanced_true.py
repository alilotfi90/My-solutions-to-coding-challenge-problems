
def tree_max_depth(root):
    def dfs(root): # we don't actually need an inner function doing it here just keep consistent with other solutions
        # null node adds no depth
        if not root:
            return 0
        # depth of current node's subtree = max depth of the two subtrees + 1 provided by current node
        return max(dfs(root.left), dfs(root.right)) + 1
    return dfs(root)
def is_balanced(tree):
    if tree is None:
        return True
    if 0<=abs(tree_max_depth(tree.left)-tree_max_depth(tree.right))<=1:
        if is_balanced(tree.left) and is_balanced(tree.right):
            return True
    return False
def main():
  print('balanced tree')
if __name__ == "__main__":
  main()