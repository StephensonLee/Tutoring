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