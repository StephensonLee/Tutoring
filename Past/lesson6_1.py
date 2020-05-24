def intersection(nums1, nums2):
    a, b = set(nums1), set(nums2)
    res = []
    for num in a:
        if num in b:
            res.append(num)
    return res

a=[4,9,5,9]
b=[9,4,9,8,4]

print (intersection(a,b))