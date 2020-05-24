
def SelectionSort(list):
    length=len(list)
    for i in range(length):
        min=i
        for j in range(i+1,length):
            if list[min]>list[j]:
                min=j
        temp=list[i]
        list[i]=list[min]
        list[min]=temp

import random
list=[5,45,12,15,9,1,36,3,78,2]

print(list)
SelectionSort(list)
print(list)
