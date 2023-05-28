# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def traverse_reverse_and_count(tree, count, k):
    if tree is None:
        return None

    answer_from_right = traverse_reverse_and_count(tree.right, count, k)
    if answer_from_right:
        return answer_from_right

    count["nodes"] += 1
    if count["nodes"] == k:
        return tree.value

    return traverse_reverse_and_count(tree.left, count, k)


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    # call on right
    # call on root
    # call on left
    # 
    count = {}
    count["nodes"] = 0
    return traverse_reverse_and_count(tree, count, k)
    return -1
