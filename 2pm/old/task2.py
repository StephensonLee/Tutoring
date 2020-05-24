# 题目：将一个正整数分解质因数。例如：输入90, 打印出90 = 2 * 3 * 3 * 5。
#


# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)
# 如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)
# 如果n <> k，但n能被k整除，则应打印出k的值，并用n除以k的商, 作为新的正整数你n, 重复执行第一步。
# (3)
# 如果n不能被k整除，则用k + 1
# 作为k的值, 重复执行第一步。
#
# 程序源代码：
#
# 实例(Python 2.0 +)

# !/usr/bin/python
# -*- coding: UTF-8 -*-

def reduceNum(n):
    while n not in [1]:  # 循环保证递归
        for index in range(2,int(n) + 1):
            if n % index == 0:
                n /= index  # n 等于 n/index
                if n == 1:
                    print(index)

                else:  # index 一定是素数
                    print('{} *'.format(index),end="")
                break


reduceNum(45635)
reduceNum(80)