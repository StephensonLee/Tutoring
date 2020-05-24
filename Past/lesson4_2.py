def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]
            # print(array)
        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]
    array[low] = key
    print(array)
    # print(array)
    return low


array2 = [5,45,12,15,9,1,36,3,78,2]
print (array2)
quick_sort_standord(array2,0,len(array2)-1)
print (array2)

# 1pm=[5,45,12,15,9,1,36,3,78,2]
# print(1pm)
# print([i for i in range(1,5)])
# quick_sort(1pm,0,len(1pm)-1)
# print(1pm)

