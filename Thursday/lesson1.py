# for i in range(10):
#     print(i)
#
# for i in range(10,-1,-1):
#     print(i)
#
# def f(a,b):
#     return a+b
#
# print(f(5,6))

# def f(i):
#     if i==1:
#         return 1
#     else:
#         return i*f(i-1)
# print(f(5))


# You are climbing a stair case.
# It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

# Examples:
# Input: 2 steps stair
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step =2 steps
# 2. 2 steps= 2 steps

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step=3 steps
# 2. 2 steps +         1 step = 3 steps
# 3. 1 step + 2 steps = 3 steps


# Input: n
# problem:
# 1.  (n-1)steps + 1 steps
# 1.  (n-2)steps + 2 steps

# order:1,2,3,4,5,6,
# value:1,2,3,5,8,13,

# ways climbing n steps=
#   ways climbing(n-1) steps + ways climbing(n-2) steps

# distinct ways to climb n stair steps:
# first case: climb 1 step at last time, climb (n-1) steps previously
# second case: climb 2 steps at last time, climb (n-2) steps previously

# ways to climb n stair=ways to climb (n-1) stair + ways to climb (n-2) stair
# initial value:
# ways to climb 1 step=1
# ways to climb 2 steps=2
# ways to climb 3 steps=1+2=3

# steps: 1,2,3,4,5,6,7,8,9,...n-2,n-1,n
# ways:  1,2,3,5,8,                   ?


def f(n):
    if n == 1:
        print(n, 1)
        return 1
    if n == 2:
        print(n, 2)
        return 2
    else:
        print(n, f(n - 1) + f(n - 2))
        return f(n - 1) + f(n - 2)


f(5)
# f(5)=f(4)+f(3)
# f(4)=f(3)+f(2)=


