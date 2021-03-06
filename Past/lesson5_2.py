def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 0 or len(nums) == 1:
        return
    i = 0
    j = i + 1
    while i < j and i < len(nums) and j < len(nums):
        if nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1

        elif nums[i] == 0 and nums[j] == 0:
            j += 1

        else:
            i += 1
            j += 1
        print(nums)
    return nums

test= [0,1,0,3,12]
print (moveZeroes(test))