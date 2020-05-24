# Serialize and Deserialize Binary Tree
# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer,
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
#
# Example:
#
# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    l = []
    stack = []
    curr = root
    while curr or stack:
        if curr:
            l.append(str(curr.val))
            stack.append(curr)
            curr = curr.left
        else:
            l.append('None')
            curr = stack.pop()
            curr = curr.right
    string = ','.join(l)
    return string

def deserialize(data):
    """Decodes your encoded data to tree.
    :type data: str
    :rtype: TreeNode
    """
    l = data.split(',')
    if len(l) <= 1:
        return None
    curr = dummy = TreeNode(-1)
    stack = [curr]
    for i in range(0, len(l)):
        if l[i] == 'None':
            nextNode = None
        else:
            nextNode = TreeNode(l[i])
        if curr:
            curr.left = nextNode
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            curr.right = nextNode
            curr = curr.right
    return dummy.left

Root=TreeNode(1)
Root.right=TreeNode(5)
cur=Root
for i in [2,3,4]:
    cur.left=TreeNode(i)
    cur=cur.left
result=serialize(Root)
print(serialize(Root))
print(deserialize(result).val)