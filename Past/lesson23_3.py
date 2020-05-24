# Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
#
# The root is the maximum number in the array.
# The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
# The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
# Construct the maximum tree by the given array and output the root node of this tree.
# Input: [3,2,1,6,0,5]
# Output: return the tree root node representing the following tree:
#
#       6
#     /   \
#    3     5
#     \    /
#      2  0
#        \
#         1


# Definition for 1pm binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructMaximumBinaryTree(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def constructTree(nums, temp):
        if (len(nums) > 0):
            temp.val = max(nums)
            index = nums.index(max(nums))
            # temp=self.cur
            if (index != 0):
                temp.left = TreeNode(None)
                constructTree(nums[:index], temp.left)
            if (index != len(nums) - 1):
                temp.right = TreeNode(None)
                constructTree(nums[index + 1:], temp.right)

    ans = TreeNode(None)
    constructTree(nums, ans)
    return ans

nums=[3,2,1,6,0,5]

print(constructMaximumBinaryTree(nums).val)