arr = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            num = 100*i+10*j+k
            if i!=j and j!=k and i!=k and num not in arr:# 互不相同且无重复数字的三位数
                arr.append(num)
print(len(arr),arr)

