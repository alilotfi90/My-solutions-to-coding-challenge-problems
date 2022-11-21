# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def is_below(topAncestor,A,B):
    if B==A or B==topAncestor:
        return True
    if A==topAncestor:
        return False
    return is_below(topAncestor,A.ancestor,B)
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    if is_below(topAncestor,descendantOne,descendantTwo):
        return descendantTwo
    if is_below(topAncestor,descendantTwo,descendantOne):
        return descendantOne
    return getYoungestCommonAncestor(topAncestor, descendantOne.ancestor, descendantTwo.ancestor)
