# 题目014：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#homework: find all factors of 1pm given number.
#example:
    # input: 9060

    # output: [2,3,3,5]


# num = int(input('number:'))
# list = []
# while num>1:
#     for i in range(2,num+1): # 因为题目是一个没写范围正整数，开方可以有效减少该值过大时候的计算量
#         if num%i==0:
#             list.append(i)
#             num = num//i
#             break
# print(list)
# print(5/2)
# print(5//22)
# print(5%2)