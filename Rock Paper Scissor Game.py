import random

user = None

computer = random.choice(['rock','paper','scissor'])

while user == None:
    print("Rock, Paper, or Scissors?")
    user = input('please enter the value: ').lower()
    if user not in ['rock','paper','scissor']:
        print('You need to choose valid value')
        user = None


if user == computer:
    print('Draw')
if user == 'rock':
    if computer == 'paper':
        print('computer wins')
    elif computer == 'scissor':
        print('user wins')
if user == 'paper':
    if computer == 'scissor':
        print('computer wins')
    elif computer == 'rock':
        print('user wins')
if user == 'scissor':
    if computer == 'rock':
        print('computer wins')
    elif computer == 'paper':
        print('user wins')

print('computer is {}'.format(computer))
print('user is {}'.format(user))
