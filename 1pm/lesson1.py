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

