a={'a':1}

a={0:1}
a={'apple':1,'pear':2}
print(a)
# adding
a['ad']=123
print(a)
# deleting
a.pop('ad')
print(a)
del(a['apple'])
print(a)

a={}
s="adhusahfaagagf"
for c in s:
    if c in a:
        a[c]+=1
    else:
        a[c]=1
print(a)

import random

target = random.randrange(1, 10)
guess=-1
while(guess!=target):
    guess = int(input("guess the number:"))
    # print (target)
    if guess>target:
        print("too high")
    elif guess<target:
        print("too low")
    else:
        print("exactly right")