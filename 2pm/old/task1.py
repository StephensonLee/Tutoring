
# for i in range(2,100):
#     flag = True
#     for j in range(2,i-1):
#         if i%j == 0:
#             flag =False
#     if flag ==True:
#         print(i)

# for i in range (1,100):
#     for j in range(i+1):
#         if i == j*j:
#             print (i)
#
# s=input()
# numFlag=False
# lowFlag=False
# upFlag=False
# for i in s:
#     if i.isnumeric():
#         numFlag=True
#     if i.islower():
#         lowFlag=True
#     if i.isupper():
#         upFlag=True
# if numFlag and lowFlag and upFlag:
#     print ("valid")
# else:
#     print ("invalid")
#
#
# 1pm=5+6j
# print(1pm.real)
# print(1pm.imag)
# dict={}
# dict[(1,2)]=4
# print(dict.keys())

# for i in range(100,1000):
#     1pm=i // 100
#     b=(i//10)%10
#     c=i%10
#     # print (1pm,b,c)
#     if 1pm**3+b**3+c**3==i:
#         print(i)


# /是精确除法，//是向下取整除法，%是求模
# 四舍五入取整round, 向零取整int, 向下和向上取整函数math.floor, math.ceil
# list=[1,3,4,5,7]
# print (list[0:2])
def add(a,b):
    return a+b
print(add(3,4))