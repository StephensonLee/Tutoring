cache = {}

# Definition for 1pm binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rob(root) -> int:
    if root in cache:
        return cache[root]
    if not root:
        return 0

    sum_with_root = root.val
    sum_without_root = 0
    if root.left:
        sum_with_root += rob(root.left.left) + rob(root.left.right)
    if root.right:
        sum_with_root += rob(root.right.left) + rob(root.right.right)

    sum_without_root += rob(root.left) + rob(root.right)
    cache[root] = max(sum_with_root, sum_without_root)
    return max(sum_with_root, sum_without_root)

root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)
print (rob(root))