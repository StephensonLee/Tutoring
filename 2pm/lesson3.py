
# 1,2,4,8,16,32,64,128,256,512,1024

# print(2**5)

sum=0
for i in range (10):
    term=2**i
    sum=sum+term
    print('i=',i,end=', ')
    print('term=',term,end=', ')
    print('sum=',sum)
print(sum)

print(1/2/2/2)

# import random
# target = random.randrange(1, 10)
# guess=-1
# while(guess!=target):
#     guess = int(input("guess the number:"))
#     # print (target)
#     if guess>target:
#         print("too high")
#     elif guess<target:
#         print("too low")
#     else:
#         print("exactly right")