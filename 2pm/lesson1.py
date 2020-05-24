print('Hello World')
print("Hello World")

print("*")
print("**")
print("***")
print("****")
print("*****")


location="Auckland"
days = 10
is_true=True
print ("I lived in Auckland.")
print ("I lived in "+location+".")
print ("I lived in %s." %location)
print ("School will reopen in 10 days")
print ("I love living in Auckland")
print ("Business will reopen in 10 days")

# Add element to list:

li=['a', 'b']
li.append('d')
print(li)

li=['a', 'b']
li.insert(0,"c")
print(li)

li=['a','b']
li.extend([2,'e'])
print(li)


# Delete element from list:
li = [1, 2, 3, 4]
del li[3]
print(li)

li = [1, 2, 3, 4]
li.pop(2)
print(li)

li = [1, 2, 3, 4]
li = li[:2] + li[3:]
print(li)

li = [1, 2, 3, 4]
li.remove(3)
print(li)



list= [4,3,2,5]
for i in range(10):
    print(i)

for i in list:
    print(i)

# write a program that prints the elements that are common between the lists
list1=[4, 5,  3,  4]
     # 0, 1,  2,  3,  4
     #-5 -4, -3, -2, -1
list2=[4,5,6,7,8]

for i in list1:
    print(i)

i=4
print(i in list2)


# def max(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
#
# print(max(3,5,4))

list=[1,2,3,4,5,3,4,5,8,4]
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)
