def bubbleSort(list):
    length= len(list)
    for i in range(length-1,-1,-1):
        for j in range(i):
            if (list[j]>list[j+1]):
                temp=list[j+1]
                list[j+1] = list[j];
                list[j] = temp;

list=[5,45,12,15,9,1,36,3,78,2]
print(list)
bubbleSort(list)
print(list)
