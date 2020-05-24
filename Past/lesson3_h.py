# words =input()
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetric(root):
    def isSym(L, R):
        if not L and not R: return True
        if L and R and L.val == R.val:
            return isSym(L.left, R.right) and isSym(L.right, R.left)
        return False

    return isSym(root, root)


print (not None)