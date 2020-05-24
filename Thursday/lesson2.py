# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Examples:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

def canJump(nums):
    if not nums or len(nums) == 0:
        return False
    reachable = [False] * len(nums)
    reachable[-1] = True  # last item is reachable if we get here

    lastTrue = len(nums) - 1  # remember the last index from right that can jump to end
    for i in reversed(range(len(nums))):
        # check if we can get to the last true from here
        if i + nums[i] >= lastTrue:  # can we get from here to the last true item?
            lastTrue = i
            reachable[i] = True

    return reachable[0]

num=[2,3,1,1,4]
print(canJump(num))