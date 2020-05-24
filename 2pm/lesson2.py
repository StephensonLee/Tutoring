# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates).
# Make sure your program works on two lists of different sizes.


import random

# for i in range(10):
#     print(random.randrange(0,10,2))

# print(random.randrange(11,21))
#
# print(random.randrange(101)/100)

import random

a=[1,3,5,7]
print(random.choice(a))

possibilities=['1','2','3']
count1=0
count2=0
count3=0
total=1000000

for i in range(total):
  outcome=random.choice(possibilities)
  if outcome=='1':
    count1+=1
  elif outcome=='2':
    count2+=1
  else:
    count3+=1
print(count1/total)
print(count2/total)
print(count3/total)

import random

a=[1,3,5,7]
print(random.choice(a))

possibilities=['Head','Tails']
countH=0
total=1000
for i in range(total):
    if random.choice(possibilities)=='Head':
        countH+=1
        print('Head')
print(countH/total)
