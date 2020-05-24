f=lambda x:2*x+1

def g (x):
    return 2*x+1

print (f(1))
print (g(1))

f= lambda x:x%3==0
test = list((i for i in range(10)))

print(list(filter(f,test)))

print (list(filter(lambda x:x%3==0 or x%4==0,test)))
print (list(map(lambda x:2*x+1,test)))
# print (list((i for i in range(100))))
