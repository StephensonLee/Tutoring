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

print('you \t vs \tcomputer')
print(your_choice+'\t vs \t'+computer_choice)

if your_choice==computer_choice:
  print('Draw')
elif your_choice=='rock' and computer_choice=='paper':
  print('You Lose')
elif your_choice=='rock' and computer_choice=='scissors':
  print('You Win')
elif your_choice=='paper' and computer_choice=='scissors':
  print('You Lose')
elif your_choice=='paper' and computer_choice=='rock':
  print('You Win')
elif your_choice=='scissors' and computer_choice=='rock':
  print('You Lose')
elif your_choice=='scissors' and computer_choice=='paper':
  print('You Win')
