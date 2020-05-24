
# 题目012：判断101-200之间有多少个素数，并输出所有素数。

'''
【个人备注】：按照素数不能被之前的素数整除，取200以内所有素数，然后取出101-200之间的部分。
'''
arr = [2,3]
# 取200以内所有素数
for i in range(4,201):
    for j in arr:
        if i%j==0:
            break
        # else: # 这是一开始我自己的写法，后来发现for可以直接接else子语句
        #     if j==arr[-1]:
        #         arr.append(i)
    else: # 迭代的对象成功迭代完，位于else的子句将执行；而如果在for循环中含有break时则直接终止循环，并不会执行else子句。
        arr.append(i)
# 取出100-200之间部分
for i in range(len(arr)):
    if arr[i]>100:
        l = arr[i:]
        print(len(l),l)
        break

for i in range(1,200):
  for j in range(2,i):
    if i%j==0:
        break
  else:
    print(i)

