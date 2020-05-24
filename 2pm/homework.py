import random


#Finding the sum of 1+2+4+8+16+...+ 512(2 to the power of 9).
sum=0
for i in range(10):
  print('sum=',sum,end=', ')
  term=2**i
  sum=sum+term
  print('i=',i,'term=',term,'sum=',sum)
print(sum)

# Follow the example, try to find the sum of 1+3+9+27+81+...+ 19683(3 to the power of 9).

