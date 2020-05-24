# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# def isSymmetric(root):
#     def isSym(L, R):
#         if not L and not R: return True
#         if L and R and L.val == R.val:
#             return isSym(L.left, R.right) and isSym(L.right, R.left)
#         return False
#
#     return isSym(root, root)
#
# Head=TreeNode(1)
# Head.left=TreeNode(2)
# Head.right=TreeNode(2)
# Head.left.left=TreeNode(4)
# Head.left.right=TreeNode(3)
# Head.right.left=TreeNode(3)
# Head.right.right=TreeNode(5)
#
# print(isSymmetric(Head))
#
# list = []
# list[0]=Head
# temp=Head.left
# while Head.left!=None:
#     list.append()
# def prt (root):
#     temp=[]
#     temp.append()

# multiples = [i for i in range(30) if i % 3 == 0]
# print(multiples)
# # Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
#
# mcase = {'1pm': 10, 'b': 34, 'A': 7, 'Z': 3}
#
# mcase_frequency = {
#     k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
#     for k in mcase.keys()
# }
#
# new_mcase ={k:mcase.get(k) for k in mcase.keys()}
# print (new_mcase)
#
# print (mcase_frequency)
# 1pm=(1,2)
# dict={1pm:1,'b':2}
# dict['c']=3
# print(dict)

# add=lambda x,y:x+y
# print (add(3,5))
#
# 1pm=[(1,2),(4,1),(9,10),(13,-3)]
# 1pm.sort(key=lambda x:x[1])
# print(1pm)

# for i in range(4):
#     for j in range(i+1,4):
#         print (i,end=' ')
#         print (j)

# 1pm=[1,2,3,4,5]
# print (min(1pm))
# list1= [1,2,3,4,5]
# list2= [5,4,3,2,1]
#
#
# data = zip(list1, list2)
# # data.sort()
# def prt(x):
#     for i in x:
#         print(i)
# # prt(data)
# prt(zip(*data))

# list1, list2 = map(lambda t: list(t), zip(*data))
# print(list1)
# print(list2)

# def inc(x):
#     return x + 10
# l = [1, 2, 3]
# print(map(inc, l))

# print (map(lambda x: x+10, l))

# def sum (x,y):
#     global result
#     result= x+y
#
# sum(3,5)
# print(result)
#
# def sum1(x,y):
#     return x+y
#
# print(sum1(3,5))

# s=['3','Asd']
# print(len(s))
# print (s[1][0].isalpha())

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# print(queue.popleft())          # The first to arrive now leaves
# # 'Eric'
# print(queue.popleft())          # The second to arrive now leaves
# # 'John'
# # queue                           # Remaining queue in order of arrival
# # deque(['Michael', 'Terry', 'Graham'])

# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# print(queue.popleft())           # The first to arrive now leaves
# # 'Eric'
# print(queue.popleft())                 # The second to arrive now leaves
# # 'John'
# # queue                           # Remaining queue in order of arrival
# # deque(['Michael', 'Terry', 'Graham'])


# 1pm=['1pm',['b','c']]
# b=['1pm',['b','c','d']]
# print(1pm>b)

# def f(1pm,b):
#     return 1pm+b,1pm-b
#
# print(f(2,3))


set1 = {"1pm", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)














