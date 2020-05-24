

# determine wether a number is a prime
# create a program that asks the user for a number and
# then prints out a list of all the divisors of that number


num=int(input())
ans=True
for i in range(2,num):
    if num%i==0:
        ans=False
        break
print(ans)


list= [1,2,3,4,5,3,4,5,8,3]
max=list[0]
for i in list:
    if i >max:
        max=i

list= [1,2,3,4,5,3,4,5,8,3]
min=list[0]
for i in list:
    if i <min:
        max=i


