sum=0
for i in range (10):
    term=2**i
    sum=sum+term
    print('i=',i,end=', ')
    print('term=',term,end=', ')
    print('sum=',sum)

print(sum)