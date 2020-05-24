def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for j in range(gap, n):
            i = j
            while (i - gap) >= 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        print (alist)
        gap //= 2


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print("original：%s" % alist)
shell_sort(alist)
print("final：%s" % alist)
