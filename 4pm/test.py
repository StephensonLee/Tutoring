import random

list=['rock','paper','scissors']

computer_choice= random.choice(list)
your_choice = input('rock(r),paper(p),scissors(s)?')

if your_choice== 'r':
  your_choice='rock'
elif your_choice=='p':
  your_choice='paper'
else:
  your_choice='scissors'


print(computer_choice)
print(your_choice)