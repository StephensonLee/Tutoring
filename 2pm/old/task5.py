# calculate the sum of 1+2!+3!+...+20! using for loop

n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)